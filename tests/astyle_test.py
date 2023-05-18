r"""Test astyle"""
import os
from pathlib import Path
from shutil import copy

import pytest

from astyle import astyle


class Test:
    r"""Test."""

    @staticmethod
    @pytest.mark.parametrize("testcase", [("input.c", "expected.c")])
    def test_astyle(testcase, tmp_path: Path) -> None:
        r"""Test astyle."""
        input, expected = testcase
        output = os.path.join(tmp_path, input)
        input = os.path.join(os.path.dirname(__file__), input)
        expected = os.path.join(os.path.dirname(__file__), expected)
        copy(input, tmp_path)
        astyle("--options=none", "--suffix=none", output)
        assert Path(output).read_text() == Path(expected).read_text()
