r"""Provide ``__version__`` for
`importlib.metadata.version() <https://docs.python.org/3/library/importlib.metadata.html#distribution-versions>`_.
"""
from pathlib import Path
from subprocess import call  # nosec: B404

BIN = str((Path(__file__).parent / "data" / "bin" / "astyle").absolute())


def astyle(*args: str) -> None:
    r"""Call astyle."""
    call([BIN] + list(args))  # nosec: B603
