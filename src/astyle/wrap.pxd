r"""Modified from ``autopxd src/astyle/wrap.h``
"""

cdef extern from "src/astyle/wrap.h":
    const char* __version__
    char* astyle_main(char* source_in, char* options)
