r"""Implement some utility functions to manage optional dependencies."""

from __future__ import annotations

__all__ = [
    "check_matplotlib",
    "check_plotly",
    "is_matplotlib_available",
    "is_plotly_available",
    "is_iden_available",
    "check_iden",
]

from importlib.util import find_spec

################
#     iden     #
################


def check_iden() -> None:
    r"""Check if the ``iden`` package is installed.

    Raises:
        RuntimeError: if the ``iden`` package is not installed.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import check_iden
    >>> check_iden()

    ```
    """
    if not is_iden_available():
        msg = (
            "`iden` package is required but not installed. "
            "You can install `iden` package with the command:\n\n"
            "pip install iden\n"
        )
        raise RuntimeError(msg)


def is_iden_available() -> bool:
    r"""Indicate if the ``iden`` package is installed or not.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import is_iden_available
    >>> is_iden_available()

    ```
    """
    return find_spec("iden") is not None


######################
#     matplotlib     #
######################


def check_matplotlib() -> None:
    r"""Check if the ``matplotlib`` package is installed.

    Raises:
        RuntimeError: if the ``matplotlib`` package is not installed.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import check_matplotlib
    >>> check_matplotlib()

    ```
    """
    if not is_matplotlib_available():
        msg = (
            "`matplotlib` package is required but not installed. "
            "You can install `matplotlib` package with the command:\n\n"
            "pip install matplotlib\n"
        )
        raise RuntimeError(msg)


def is_matplotlib_available() -> bool:
    r"""Indicate if the ``matplotlib`` package is installed or not.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import is_matplotlib_available
    >>> is_matplotlib_available()

    ```
    """
    return find_spec("matplotlib") is not None


##################
#     plotly     #
##################


def check_plotly() -> None:
    r"""Check if the ``plotly`` package is installed.

    Raises:
        RuntimeError: if the ``plotly`` package is not installed.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import check_plotly
    >>> check_plotly()

    ```
    """
    if not is_plotly_available():
        msg = (
            "`plotly` package is required but not installed. "
            "You can install `plotly` package with the command:\n\n"
            "pip install plotly\n"
        )
        raise RuntimeError(msg)


def is_plotly_available() -> bool:
    r"""Indicate if the ``plotly`` package is installed or not.

    Example usage:

    ```pycon

    >>> from startorch.utils.imports import is_plotly_available
    >>> is_plotly_available()

    ```
    """
    return find_spec("plotly") is not None
