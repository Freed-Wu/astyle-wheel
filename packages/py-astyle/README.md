# Astyle python port

This project provides python port for [astyle](https://gitlab.com/saalen/astyle).

## Install

```shell
pip install py-astyle
```

## Usage

```python
from astyle import astyle

astyle("  #include <Python.h>", "indent-classes")
```

### Alternatives

- [pyastyle](https://github.com/timonwong/pyastyle): stop maintaining.
