# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for extracting version information from package metadata.

"""
import importlib.metadata
import json
import logging
import pathlib
import re
import subprocess
import sys
from typing import Optional, Union

import requests

from .exceptions import InvalidVersionError, QbraidSystemError, VersionNotFoundError

if sys.version_info >= (3, 11):
    import tomllib

    MODE = "rb"
else:
    try:
        import toml as tomllib

        MODE = "r"
    except ImportError:
        tomllib = None
        MODE = "r"


logger = logging.getLogger(__name__)


def is_valid_semantic_version(v: str) -> bool:
    """
    Returns True if given string represents a valid
    semantic version, False otherwise.

    """
    try:
        # pylint: disable-next=import-outside-toplevel
        from packaging.version import InvalidVersion, Version

        Version(v)
        return True
    except ImportError:
        # Fallback to regex matching if packaging is not installed
        semantic_version_pattern = re.compile(
            r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
            r"(-([0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*))?"
            r"(\+([0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*))?$"
        )
        return bool(semantic_version_pattern.match(v))
    except InvalidVersion:
        return False


def _get_version_from_json(package_json_path: Union[str, pathlib.Path]) -> str:
    """Get the version from the package.json file."""
    try:
        with open(package_json_path, "r", encoding="utf-8") as file:
            pkg_json = json.load(file)
            return pkg_json["version"]
    except (FileNotFoundError, KeyError, IOError) as err:
        raise VersionNotFoundError("Unable to find or read package.json") from err


def _simple_toml_version_extractor(file_path: Union[str, pathlib.Path]) -> str:
    """
    Extract the version from a pyproject.toml file using simple string processing.
    This function assumes the version is under [project] and is labeled as version = "x.y.z".
    It is a very basic and fragile implementation and not recommended for general TOML parsing.
    """
    version_pattern = re.compile(r'^version\s*=\s*"([^"]+)"$', re.M)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        match = version_pattern.search(content)
        if match:
            return match.group(1)
        raise ValueError("Version key not found in the TOML content.")
    except FileNotFoundError as err:
        raise VersionNotFoundError("The specified TOML file does not exist.") from err
    except IOError as err:
        raise VersionNotFoundError("An error occurred while reading the TOML file.") from err


def _get_version_from_toml(pyproject_toml_path: Union[str, pathlib.Path]) -> str:
    """Get the version from the pyproject.toml file."""
    if tomllib is None:
        return _simple_toml_version_extractor(pyproject_toml_path)

    try:
        with open(pyproject_toml_path, MODE) as file:
            pyproject_toml = tomllib.load(file)
            return pyproject_toml["project"]["version"]
    except (FileNotFoundError, KeyError, IOError) as err:
        raise VersionNotFoundError("Unable to find or read pyproject.toml") from err


def extract_version(
    file_path: Union[str, pathlib.Path], shorten_prerelease: bool = False, check: bool = False
) -> str:
    """Extract the version from a given package.json or pyproject.toml file.

    Args:
        file_path (Union[str, pathlib.Path]): Path to the package metadata file.
        shorten_prerelease (bool): Whether to shorten the prerelease version.
        check (bool): Whether to check if the version is a valid semantic version.

    Returns:
        str: The version extracted from the file.


    Raises:
        ValueError: If the file type is not supported.
        InvalidVersionError: If the version is not a valid semantic version.
        VersionNotFoundError: If the version is not found in the file.
    """
    if not isinstance(shorten_prerelease, bool):
        raise TypeError("shorten_prerelease must be a boolean.")

    if not isinstance(check, bool):
        raise TypeError("check must be a boolean.")

    file_path = pathlib.Path(file_path)

    if file_path.suffix == ".json":
        version = _get_version_from_json(file_path)
    elif file_path.suffix == ".toml":
        version = _get_version_from_toml(file_path)
    else:
        raise ValueError(
            "Unsupported file type. Only package.json and pyproject.toml are supported."
        )

    if shorten_prerelease:
        version = version.replace("-alpha.", "a").replace("-beta.", "b").replace("-rc.", "rc")

    if check and not is_valid_semantic_version(version):
        raise InvalidVersionError(f"Invalid semantic version: {version}")

    return version


def get_latest_package_version(package: str, prerelease: bool = False) -> str:
    """Retrieves the latest version of package from PyPI."""
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as err:
        raise VersionNotFoundError(
            f"Failed to retrieve latest {package} version from PyPI."
        ) from err

    data = response.json()

    if not prerelease:
        try:
            return data["info"]["version"]
        except KeyError as err:
            raise QbraidSystemError(
                f"Failed to extract version from {package} package metadata."
            ) from err

    try:
        all_versions = list(data["releases"].keys())
    except KeyError as err:
        raise QbraidSystemError(
            f"Failed to extract version from {package} package metadata."
        ) from err

    if len(all_versions) == 0:
        raise VersionNotFoundError(f"No versions found for {package}")

    latest_version = all_versions[-1]
    return latest_version


def get_local_package_version(
    package: str, python_path: Optional[Union[str, pathlib.Path]] = None
) -> str:
    """Retrieves the local version of a package."""
    if python_path:
        try:
            result = subprocess.run(
                [
                    str(python_path),
                    "-c",
                    f"import importlib.metadata; print(importlib.metadata.version('{package}'))",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as err:
            raise QbraidSystemError(f"{package} not found in the current environment.") from err
        except FileNotFoundError as err:
            raise QbraidSystemError(f"Python executable not found at {python_path}.") from err

    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError as err:
        raise QbraidSystemError(f"{package} not found in the current environment.") from err


def get_bumped_version(latest: str, local: str) -> str:
    """Compare latest and local versions and return the bumped version."""
    # pylint: disable-next=import-outside-toplevel
    from packaging.version import Version, parse

    latest_version = parse(latest)
    local_version = parse(local)

    def bump_prerelease(version: Version) -> str:
        if version.pre:
            pre_type, pre_num = version.pre[0], version.pre[1]
            return f"{version.base_version}-{pre_type}.{pre_num + 1}"
        return f"{version.base_version}-a.0"

    if local_version.base_version > latest_version.base_version:
        return f"{local_version.base_version}-a.0"
    if local_version.base_version == latest_version.base_version:
        if latest_version.is_prerelease:
            if local_version.is_prerelease:
                if local_version.pre[0] == latest_version.pre[0]:
                    if local_version.pre[1] > latest_version.pre[1]:
                        raise InvalidVersionError(
                            "Local version prerelease is newer than latest version."
                        )
                    return bump_prerelease(latest_version)
                if local_version.pre[0] < latest_version.pre[0]:
                    return bump_prerelease(latest_version)
                return f"{local_version.base_version}-{local_version.pre[0]}.0"
            raise InvalidVersionError("Latest version is prerelease but local version is not.")
        if local_version.is_prerelease:
            return f"{local_version.base_version}-{local_version.pre[0]}.0"
        if local_version == latest_version:
            return f"{local_version.base_version}-a.0"
        raise InvalidVersionError(
            "Local version base is equal to latest, but no clear upgrade path found."
        )
    raise InvalidVersionError("Latest version base is greater than local, cannot bump.")


def compare_versions(version1: Optional[str], version2: Optional[str]) -> str:
    """
    Compare two semantic version strings and return the greater one.

    Args:
        version1 (Optional[str]): The first semantic version string.
        version2 (Optional[str]): The second semantic version string.

    Returns:
        str: The greater of the two versions. If both versions are None, None is returned.
             If one version is None and the other isn't, a defined value is returned.

    Raises:
        ValueError: If both versions are None.
    """
    # pylint: disable-next=import-outside-toplevel
    from packaging.version import parse

    if version1 is None and version2 is None:
        raise ValueError("Both versions are None.")

    if version1 is None:
        return version2
    if version2 is None:
        return version1

    v1 = parse(version1)
    v2 = parse(version2)

    if v1 > v2:
        return version1
    if v2 > v1:
        return version2

    logger.debug("Versions %s and %s are equal.", version1, version2)
    return version1


def get_prelease_version(
    project_root: Union[pathlib.Path, str], package_name: str, shorten: bool = True
) -> str:
    """
    Determine the bumped version of a package based on local and latest versions.

    Args:
        project_root (pathlib.Path): Path to the project root directory.
        package_name (str): Name of the package to check.
        shorten (bool): Flag to determine if prerelease versions should be shortened.

    Returns:
        str: The bumped version string.

    """
    project_root = pathlib.Path(project_root)
    pyproject_toml_path = project_root / "pyproject.toml"

    if not pyproject_toml_path.exists():
        raise FileNotFoundError("pyproject.toml not found")

    v_local = extract_version(pyproject_toml_path, shorten_prerelease=shorten)
    v_latest_pre = get_latest_package_version(package_name, prerelease=True)
    v_latest_stable = get_latest_package_version(package_name, prerelease=False)
    v_latest = compare_versions(v_latest_pre, v_latest_stable)
    v_prerelease = get_bumped_version(v_latest, v_local)
    return v_prerelease


__all__ = [
    "extract_version",
    "get_bumped_version",
    "get_latest_package_version",
    "get_local_package_version",
    "is_valid_semantic_version",
    "compare_versions",
    "get_prelease_version",
]
