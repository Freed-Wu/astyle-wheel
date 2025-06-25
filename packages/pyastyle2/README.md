# Astyle python binding

This project provides python binding for
[astyle](https://gitlab.com/saalen/astyle).

## Install

```shell
pip install pyastyle2
```

## Usage

```python
from astyle import astyle

astyle("  #include <Python.h>", "indent-classes")
```

### Alternatives

- [pyastyle](https://github.com/timonwong/pyastyle): stop maintaining.
