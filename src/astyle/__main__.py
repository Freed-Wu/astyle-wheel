r"""This module can be called by
`python -m <https://docs.python.org/3/library/__main__.html>`_.
"""
import sys

from . import astyle


def main() -> None:
    r"""Call astyle."""
    astyle(*sys.argv[1:])


if __name__ == "__main__":
    main()
