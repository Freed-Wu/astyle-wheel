r"""Test astyle"""

import os
import sys
from pathlib import Path
from shutil import copy

import pytest


class Test:
    r"""Test."""

    @staticmethod
    @pytest.mark.parametrize("testcase", [("input.c", "expected.c")])
    @pytest.mark.skipif(
        sys.platform == "win32",
        reason="binary module build failure on windows",
    )
    def test_astyle(testcase, tmp_path: Path) -> None:
        r"""Test astyle."""
        from astyle.__main__ import main

        input, expected = testcase
        output = os.path.join(tmp_path, input)
        input = os.path.join(os.path.dirname(__file__), input)
        expected = os.path.join(os.path.dirname(__file__), expected)
        copy(input, tmp_path)
        assert main("--options=none", "--suffix=none", output) == 0
        assert Path(output).read_text() == Path(expected).read_text()
