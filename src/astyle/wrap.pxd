r"""Run ``autopxd src/astyle/wrap.h``"""

cdef extern from "src/astyle/wrap.h":

    const char* AStyleGetVersion()

    char* astyle_main(char* source_in, char* options)
