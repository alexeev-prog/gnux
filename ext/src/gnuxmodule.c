#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *gnux_system(PyObject *self, PyObject *args) {
	const char *command;
	int sts;

	if (!PyArg_ParseTuple(args, "s", &command)) {
		return NULL;
	}
	sts = system(command);
	return PyLong_FromLong(sts);
}

static PyMethodDef GNUXMethods[] = { { "exec_shell_command", gnux_system, METH_VARARGS,
									   "Execute a shell command." },
									 { NULL, NULL, 0, NULL } };

static struct PyModuleDef gnuxmodule = { PyModuleDef_HEAD_INIT, "ext", NULL, -1, GNUXMethods };

PyMODINIT_FUNC PyInit_ext(void) { return PyModule_Create(&gnuxmodule); }
