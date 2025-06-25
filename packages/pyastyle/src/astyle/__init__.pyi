r"""Provide ``__version__`` for
`importlib.metadata.version() <https://docs.python.org/3/library/importlib.metadata.html#distribution-versions>`_.
Keep this file for type annotation.
"""

from cython.cimports.wrap import (  # type: ignore
    AStyleGetVersion,  # noqa: F401
    astyle_main,
)

__version__ = AStyleGetVersion().decode()


def astyle(source_in: str, options: str = "") -> str:
    r"""Python port of astyle.

    :param source_in: source code
    :type source_in: str
    :param options: such as "indent-classes"
    :type options: str
    :rtype: str
    """
    return astyle_main(source_in.encode(), options.encode()).decode()
