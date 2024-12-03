#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

int make_directory(const char *path) {
	int result = mkdir(path, 0777);
	if (result == 0) {
		printf("\033[0;32mSuccess:\033[0m Directory '%s' created.\n", path);
	} else {
		printf("\033[0;31mError:\033[0m Failed to create directory '%s'.\n", path);
		exit(1);
	}

	return result;
}

void create_parent_directories(const char *path) {
	char *path_copy = strdup(path);
	char *token = strtok(path_copy, "/");
	char *directory_path = NULL;

	while (token != NULL) {
		if (directory_path == NULL) {
			directory_path = strdup(token);
		} else {
			size_t length = strlen(directory_path) + strlen(token) + 2;
			char *temp = (char *)malloc(length);
			snprintf(temp, length, "%s/%s", directory_path, token);
			free(directory_path);
			directory_path = temp;
		}

		make_directory(directory_path);
		token = strtok(NULL, "/");
	}

	free(directory_path);
	free(path_copy);
}

static PyObject *gnux_mkdir(PyObject *self, PyObject *args) {
	const char *dir_name;

	if (!PyArg_ParseTuple(args, "s", &dir_name)) {
		return NULL;
	}

	int status = 0;

	create_parent_directories(dir_name);

	return PyLong_FromLong(status);
}

static PyMethodDef MKDIRMethods[] = { { "gnux_mkdir", gnux_mkdir, METH_VARARGS,
										"Create directory (ignore_exists is exist_ok)" },
									  { NULL, NULL, 0, NULL } };

static struct PyModuleDef mkdirmodule = { PyModuleDef_HEAD_INIT, "mkdir", NULL, -1, MKDIRMethods };

PyMODINIT_FUNC PyInit_mkdir(void) { return PyModule_Create(&mkdirmodule); }
