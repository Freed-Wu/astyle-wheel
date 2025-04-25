# Astyle Python Distribution

This project packages the [astyle](https://gitlab.com/saalen/astyle) utility as
a Python package.

## Install

```shell
pip install astyle
```

## Usage

### shell

```shell
astyle --help
# or
python -m astyle --help
```

### python

```python
from astyle.__main__ import main

main("--help")
```

Or:

```python
from astyle import astyle

astyle("  #include <Python.h>", "indent-classes")
```

### pre-commit

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Freed-Wu/astyle-wheel
    rev: 3.6.9
    hooks:
      - id: astyle
```
