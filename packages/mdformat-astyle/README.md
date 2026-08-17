# Astyle python binding

This project provides python binding for
[astyle](https://gitlab.com/saalen/astyle).

## Install

```shell
pip install mdformat-astyle
```

## API

```python
from astyle.binding import astyle

astyle("  #include <Python.h>", "indent-classes")
```

## Usage

``````markdown
```c astyle=mode=kr,indent=2
#include <Python.h>
```
``````

```sh
pip install mdformat mdformat-astyle
mdformat
```

### Alternatives

- [pyastyle](https://github.com/timonwong/pyastyle): stop maintaining.
