#!/usr/bin/env python3

import faulthandler
import functools
import os

from debian import debian_support
from launchpadlib.launchpad import Launchpad
from launchpadlib.uris import service_roots

faulthandler.enable()


def _get_binary_package_publishing_histories(archive, version, binary_package_name, distro_arch_series=None):
    binary_publish_histories = archive.getPublishedBinaries(
        exact_match=True,
        version=version,
        binary_name=binary_package_name,
        order_by_date=True,
        distro_arch_series=distro_arch_series,
    )
    return binary_publish_histories


def _get_binary_build(archive, launchpad, lp_arch_series, package_name,
                     package_version):
    binary_publishing_histories = _get_binary_package_publishing_histories(
        archive, package_version, package_name, distro_arch_series=lp_arch_series
    )
    binary_build = None
    binary_publishing_history = None
    if len(binary_publishing_histories):
        # we don't filter the getPublishedBinaries query by distro_arch_series as
        # the version we are querying might have been built for a previous release
        # instead we can filter the builds on the arch tag
        binary_publishing_history = binary_publishing_histories[0]
        binary_build_link = binary_publishing_history.build_link
        try:
            binary_build = launchpad.load(binary_build_link)
            print(
                f"INFO: \tFound binary package "
                f"{package_name} {lp_arch_series.architecture_tag} version {package_version} in {lp_arch_series.display_name} build."
            )
        except ValueError:
            print(
                f"**********ERROR(Exception): \tCould not load binary build link {binary_build_link}."
            )
    return binary_build, binary_publishing_history


def download_deb(
    package_name, package_version, package_architecture="amd64", series=None, fallback=False):
    """
    Download a deb from launchpad for a specific package version and architecture
    """
    if f":{package_architecture}" in package_name:
        # strip the architecture from the package name if it is present
        package_name = package_name.replace(f":{package_architecture}", "")
    # Log in to launchpad annonymously - we use launchpad to find
    # the package publish time
    launchpad = Launchpad.login_anonymously(
        "ubuntu-package-download", service_root=service_roots["production"], version="devel"
    )

    ubuntu = launchpad.distributions["ubuntu"]
    archive = ubuntu.main_archive
    lp_series = ubuntu.getSeries(name_or_version=series)
    # For the package we care about none in `main` that I have found were built prior to 14.04 so we
    # can use this as a cut off point
    series_cut_off_version = "14.04"
    # This will be our fallback if we do not find a build for the specified architecture
    architecture_all_arch_tag = "amd64"

    lp_arch_series = lp_series.getDistroArchSeries(archtag=package_architecture)

    binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, lp_arch_series, package_name, package_version)

    if binary_build and binary_publishing_history:
        _perform_download(binary_build, binary_publishing_history, launchpad, lp_series)
        return
    else:
        print(
            f"WARNING: \tCould not find binary package {package_name} {package_architecture} version {package_version} in series {series}."
        )
        if package_architecture != architecture_all_arch_tag:
            print(
                f"INFO: \tFALLBACK - Attempting to find and download the {package_name} {architecture_all_arch_tag} version {package_version}..."
            )
            binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, lp_arch_series, package_name, package_version)
            if binary_build and binary_publishing_history:
                _perform_download(binary_build, binary_publishing_history, launchpad, lp_series)
                return

        # before we attempt to fallback to a different versions we should check if there are any builds for the
        # same version but for a different series
        all_series = ubuntu.series_collection
        for fallback_series in all_series:
            if (fallback_series.name != series
                and fallback_series.version <= lp_series.version
                and fallback_series.version >= series_cut_off_version):
                fallback_lp_arch_series = fallback_series.getDistroArchSeries(archtag=package_architecture)
                print(
                    f"INFO: \tFALLBACK TO PREVIOUS SERIES - Attempting to find and download the {package_name} version {package_version} from {fallback_series.name}..."
                )
                binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, fallback_lp_arch_series,
                                                                            package_name, package_version)
                if binary_build and binary_publishing_history:
                    _perform_download(binary_build, binary_publishing_history, launchpad, fallback_series)
                    # we have found our package so we can break from the loop
                    return
                else:
                    print(
                        f"WARNING: \tCould not find binary package {package_name} {package_architecture} version {package_version} in series {fallback_series.name}."
                    )
                    if package_architecture != architecture_all_arch_tag:
                        print(
                            f"INFO: \tFALLBACK TO PREVIOUS SERIES - Attempting to find and download the {package_name} {architecture_all_arch_tag} version {package_version} from {fallback_series.name}..."
                        )
                        binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, fallback_lp_arch_series,
                                                                                    package_name, package_version)
                        if binary_build and binary_publishing_history:
                            _perform_download(binary_build, binary_publishing_history, launchpad, fallback_series)
                            return

        print(
            f"WARNING: \tCould not find binary package {package_name} {package_architecture} version {package_version} for any Ubuntu series."
        )
        print(
            f"INFO: \tFALLBACK TO PREVIOUS VERSION - Attempting to find and download the next version of "
            f"{package_name} {package_architecture}..."
        )
        if fallback:
            fallback_lp_series = ubuntu.getSeries(name_or_version=series)
            fallback_lp_arch_series = fallback_lp_series.getDistroArchSeries(archtag=package_architecture)

            binary_publishing_histories_all_versions = _get_binary_package_publishing_histories(
                archive, None, package_name, distro_arch_series=fallback_lp_arch_series
            )
            if len(binary_publishing_histories_all_versions):
                next_binary_package_version = None
                previous_binary_package_version = None
                build_package_versions = []
                for binary_publishing_history in binary_publishing_histories_all_versions:
                    build_package_version = binary_publishing_history.binary_package_version
                    build_package_versions.append(build_package_version)

                # now sort the versions and find the next version
                sorted_build_package_versions = sorted(build_package_versions, reverse=True,
                                                       key=functools.cmp_to_key(debian_support.version_compare))
                for build_package_version in sorted_build_package_versions:

                    version_comparison = debian_support.version_compare(build_package_version,
                                                                        package_version)
                    if version_comparison >= 0:
                        """
                        > 0 The version build_package_version is greater than version package_version.

                        = 0 Both versions are equal.

                        < 0 The version current_package_version is less than version previous_package_version.
                        """
                        next_binary_package_version = build_package_version
                    elif version_comparison < 0:
                        # This is a version lower than the current version so we can break from the
                        # loop knowing that we now know the previous version that has a build publishing history
                        previous_binary_package_version = build_package_version
                        # The list is sorted is descending order so we can break once we find the first version
                        # that is lower than the queried version.
                        break

                if next_binary_package_version:
                    print(
                        f"INFO: \tFALLBACK TO NEXT VERSION - Found next version {next_binary_package_version} of {package_name} {package_architecture} (queried version was {package_version})."
                    )
                    # download_deb(
                    #     package_name, next_binary_package_version, package_architecture
                    # )
                    binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, lp_arch_series,
                                                                                package_name, next_binary_package_version)
                    if binary_build and binary_publishing_history:
                        _perform_download(binary_build, binary_publishing_history, launchpad, lp_series)
                        return

                elif not next_binary_package_version and previous_binary_package_version:
                    print(
                        f"INFO: \tFALLBACK TO PREVIOUS VERSION - Version in same series {series} of {package_name} greater than queried version {package_version} was not found."
                    )
                    print(
                        f"INFO: \tFALLBACK TO PREVIOUS VERSION - Found previous version {previous_binary_package_version} of {package_name} {package_architecture} in series {series} (queried version was {package_version})."
                    )
                    binary_build, binary_publishing_history = _get_binary_build(archive, launchpad, lp_arch_series,
                                                                                package_name,
                                                                                previous_binary_package_version)
                    if binary_build and binary_publishing_history:
                        _perform_download(binary_build, binary_publishing_history, launchpad, lp_series)
                        return
        print("ERROR: \tCould not find a fallback version to download.")


def _perform_download(binary_build, binary_publishing_history, launchpad, lp_series):
    binary_build_urls = binary_publishing_history.binaryFileUrls()
    for binary_build_url in binary_build_urls:
        binary_build_filename = binary_build_url.split("/")[-1]
        # only download the deb file if it doesn't already exist
        if not os.path.isfile(binary_build_filename):
            with open(binary_build_filename, "wb") as f:
                f.write(launchpad._browser.get(binary_build_url))
                print(
                    f"INFO: \tDownloaded {binary_build_filename} from {lp_series.name} {binary_build.arch_tag} build.")
        else:
            print(f"INFO: \t{binary_build_filename} already exists.")
