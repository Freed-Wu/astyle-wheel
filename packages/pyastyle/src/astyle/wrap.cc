#include <Python.h>
#include <astyle_main.h>

#include "wrap.h"

static void STDCALL errorHandler(int errorNumber, const char *errorMessage) {
    PyErr_SetString(PyExc_ValueError, errorMessage);
}

static char *STDCALL memoryAlloc(unsigned long memoryNeeded) {
    return new char[memoryNeeded];
}

char *astyle_main(char *source_in, char *options) {
    return AStyleMain(source_in, options, errorHandler, memoryAlloc);
}
