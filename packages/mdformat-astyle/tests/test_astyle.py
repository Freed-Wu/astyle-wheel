r"""Test astyle."""

from astyle.binding import astyle
from astyle.mdformat import mdformat


class Test:
    r"""Test."""

    @staticmethod
    def test_binding() -> None:
        assert astyle("  #include <stdio.h>") == "#include <stdio.h>"

    @staticmethod
    def test_mdformat() -> None:
        assert (
            mdformat("  #include <stdio.h>", "c astyle=style=kr")
            == "#include <stdio.h>"
        )
