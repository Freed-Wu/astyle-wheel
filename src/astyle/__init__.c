#include <Python.h>

#include "wrap.h"

extern const char *__version__;

static PyObject *binding(PyObject *self, PyObject *args, PyObject *kwargs) {
    static char *keywords[] = {"source_in", "options", NULL};
    char *source_in, *options = NULL;
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s|s", keywords, &source_in,
                                     &options))
        return NULL;
    if (!options)
        options = "";
    char *output = astyle_main(source_in, options);
    if (!output) {
        PyErr_SetString(PyExc_ValueError, "failed to format input source");
        return NULL;
    }
    return PyUnicode_FromString(output);
}

static PyMethodDef methods[] = {
    {"astyle", (PyCFunction)binding, METH_VARARGS | METH_KEYWORDS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {PyModuleDef_HEAD_INIT, "astyle", NULL, -1,
    methods
};

PyMODINIT_FUNC PyInit_astyle(void) {
    PyObject *m = PyModule_Create(&module);
    PyModule_AddStringConstant(m, "__version__", __version__);
    return m;
}
