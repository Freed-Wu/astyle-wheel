r"""Test binding."""

from astyle.binding import astyle
from astyle.mdformat import mdformat


class Test:
    r"""Test."""

    @staticmethod
    def test_astyle() -> None:
        assert astyle("  #include <stdio.h>") == "#include <stdio.h>"
        assert (
            mdformat("  #include <stdio.h>", "c astyle=style=kr")
            == "#include <stdio.h>"
        )
