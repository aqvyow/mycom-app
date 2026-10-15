"""Lab package.

The version is read from installed distribution metadata so that stamping the
version into ``pyproject.toml`` at build time is the single source of truth.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

DISTRIBUTION = "mycom-app"


def __version__() -> str:
    try:
        return version(DISTRIBUTION)
    except PackageNotFoundError:  # running from a source checkout
        return "0.0.0+unknown"


__all__ = ["DISTRIBUTION", "__version__"]
