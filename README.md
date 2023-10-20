# Astyle Python distribution

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/astyle-wheel/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/astyle-wheel/main)
[![github/workflow](https://github.com/Freed-Wu/astyle-wheel/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/astyle-wheel/actions)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/astyle-wheel/total)](https://github.com/Freed-Wu/astyle-wheel/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/astyle-wheel/latest/total)](https://github.com/Freed-Wu/astyle-wheel/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)
[![github/v](https://shields.io/github/v/release/Freed-Wu/astyle-wheel)](https://github.com/Freed-Wu/astyle-wheel)

[![pypi/status](https://shields.io/pypi/status/astyle)](https://pypi.org/project/astyle/#description)
[![pypi/v](https://shields.io/pypi/v/astyle)](https://pypi.org/project/astyle/#history)
[![pypi/downloads](https://shields.io/pypi/dd/astyle)](https://pypi.org/project/astyle/#files)
[![pypi/format](https://shields.io/pypi/format/astyle)](https://pypi.org/project/astyle/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/astyle)](https://pypi.org/project/astyle/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/astyle)](https://pypi.org/project/astyle/#files)

This project packages the [astyle](https://gitlab.com/saalen/astyle) utility as
a Python package.

## Install

```shell
pip install astyle
```

Installing is not needed for [pre-commit](https://pre-commit.com/).

## Usage

### shell

```shell
astyle --help
# or
python -m astyle --help
```

### python

```python
from astyle import astyle

astyle("--help")
```

### pre-commit

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Freed-Wu/mirrors-astyle
    rev: 3.4.9
    hooks:
      - id: astyle
```

```shell
pre-commit install
git commit
```

Please use <https://github.com/Freed-Wu/mirrors-astyle>, it uses binary wheel
and will be faster than this repository which uses source code.

## Similar Projects

### pre-commit hooks

- [mirrors-clang-format](https://github.com/pre-commit/mirrors-clang-format)
- [CLinters](https://github.com/pocc/pre-commit-hooks): it requires you install
  linters and formatters in your machine and it calls them. So it cannot
  ensure the versions of linters and formatters are same as others, which means
  it cannot ensure **reproducibility**.
- [astyle_precommit_hook](https://github.com/mellowcandle/astyle_precommit_hook):
  it uses git hook, not pre-commit, which make it cannot use many hooks at the
  same time. It cannot ensure **reproducibility**, too.
- [pyastyle](https://github.com/timonwong/pyastyle): stop maintaining.
- [astyle_py](https://github.com/igrr/astyle_py): it uses wasm, not native
  binary programs like this project.

### Python distributions

- [clang-format-wheel](https://github.com/ssciwr/clang-format-wheel)
- [cmake-python-distributions](https://github.com/scikit-build/cmake-python-distributions)
- [ninja-python-distributions](https://github.com/scikit-build/ninja-python-distributions)
