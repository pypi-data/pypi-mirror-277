/*
 * Copyright © 2024 Contrast Security, Inc.
 * See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
 */
/* Python requires its own header to always be included first */
#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <contrast/assess/patches.h>
#include <contrast/assess/scope.h>
#include <contrast/assess/intern.h>
#include <contrast/assess/logging.h>
#include <contrast/assess/trace.h>

static PyMethodDef methods[] = {
    {"initialize_logger",
     (PyCFunction)initialize_logger,
     METH_VARARGS | METH_KEYWORDS,
     "Initialize C extension logger"},
    {"initialize",
     (PyCFunction)initialize,
     METH_NOARGS,
     "Initialize C extension patcher"},
    {"enable_required_hooks",
     enable_required_hooks,
     METH_O,
     "Hook relevant non-method functions"},
    {"has_funchook",
     has_funchook,
     METH_NOARGS,
     "Return bool indicating whether funchook is available"},
    {"initialize_trace",
     initialize_trace,
     METH_NOARGS,
     "Initialize trace for string propagation"},
#ifndef NO_FUNCHOOK
    {"create_unicode_hook_module",
     create_unicode_hook_module,
     METH_NOARGS,
     "Create table of unicode method hook functions"},
    {"create_bytes_hook_module",
     create_bytes_hook_module,
     METH_NOARGS,
     "Create table of bytes method hook functions"},
    {"create_bytearray_hook_module",
     create_bytearray_hook_module,
     METH_NOARGS,
     "Create table of bytearray method hook functions"},
#endif
    {"install", install, METH_O, "Install string hooks"},
    {"disable", disable, METH_O, "Remove all hooks"},
    {"set_exact_scope",
     set_exact_scope,
     METH_O,
     "Sets the scope exactly what you pass to it"},
    {"enter_scope", enter_scope, METH_VARARGS, "Enter given scope"},
    {"exit_scope", exit_scope, METH_VARARGS, "Exit given scope"},
    {"in_scope", in_scope, METH_VARARGS, "Check whether in given scope"},
    {"in_contrast_or_propagation_scope",
     in_contrast_or_propagation_scope,
     METH_NOARGS,
     "Check in propagation (or contrast) scope"},
    {"get_current_scope",
     get_current_scope,
     METH_NOARGS,
     "Get scope levels from current active Context"},
    {"init_contrast_scope_cvars",
     init_contrast_scope_cvars,
     METH_NOARGS,
     "Initialize ContextVars used for scope"},
    {"get_tp_version_tag", get_tp_version_tag, METH_O, "Get tp_version_tag for a type"},
    {"set_attr_on_type", set_attr_on_type, METH_VARARGS, "Set attribute on type"},
    {"is_string_interned", is_string_interned, METH_O, "Checks if string is interned"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef cs_str_definition = {
    PyModuleDef_HEAD_INIT,
    "cs_str",
    "description here",
    -1,
    methods,
    NULL,
    NULL,
    NULL,
    NULL};

PyMODINIT_FUNC PyInit_cs_str(void) {
    PyObject *module;

    Py_Initialize();

    module = PyModule_Create(&cs_str_definition);

    PyModule_AddIntConstant(module, "CONTRAST_SCOPE", CONTRAST_SCOPE);
    PyModule_AddIntConstant(module, "PROPAGATION_SCOPE", PROPAGATION_SCOPE);
    PyModule_AddIntConstant(module, "TRIGGER_SCOPE", TRIGGER_SCOPE);

    return module;
}
