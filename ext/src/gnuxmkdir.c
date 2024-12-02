#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <sys/stat.h>
#include <errno.h>

static PyObject *gnux_mkdir(PyObject *self, PyObject *args)
{
	const char* dir_name;
	int ignore_exists;

	if (!PyArg_ParseTuple(args, "si", &dir_name, &ignore_exists))
	{
		return NULL;
	}

	int status = mkdir(dir_name, 0755);

	if (errno == EEXIST && ignore_exists) {
		return PyLong_FromLong(0);
	} else if (status != 0 && !ignore_exists) {
		PyErr_SetFromErrno(PyExc_OSError);
		return NULL;
	}

	return PyLong_FromLong(status);
}

static PyMethodDef MKDIRMethods[] = {
	{"gnux_mkdir", gnux_mkdir, METH_VARARGS, "Create directory (ignore_exists is exist_ok)"},
	{NULL, NULL, 0, NULL}};

static struct PyModuleDef mkdirmodule = {PyModuleDef_HEAD_INIT, "mkdir", NULL, -1, MKDIRMethods};

PyMODINIT_FUNC PyInit_mkdir(void)
{
	return PyModule_Create(&mkdirmodule);
}

