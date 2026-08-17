r"""Mdformat
============
"""

from shlex import split

from .binding import astyle


def mdformat(source_in: str, info: str = "c") -> str:
    opts = split(info)
    if opts[0] not in ["java", "cs"]:
        opts[0] = "c"
    options = "mode=" + opts[0]
    for opt in opts[1:]:
        if opt.startswith("astyle="):
            options += " " + opt[len("astyle=") :]
    return astyle(source_in, options)
