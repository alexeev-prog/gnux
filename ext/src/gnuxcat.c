#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>

#define BLUE_COLOR "\033[34m"
#define RESET_COLOR "\033[0m"
#define LINE_LENGTH 512

void printFileDetails(const char *filename) {
	struct stat fileStat;
	if (stat(filename, &fileStat) < 0) {
		perror("stat");
		return;
	}

	printf("\nFile Details:\n");
	printf("File Permissions: ");
	printf((S_ISDIR(fileStat.st_mode)) ? "d" : "-");
	printf((fileStat.st_mode & S_IRUSR) ? "r" : "-");
	printf((fileStat.st_mode & S_IWUSR) ? "w" : "-");
	printf((fileStat.st_mode & S_IXUSR) ? "x" : "-");
	printf((fileStat.st_mode & S_IRGRP) ? "r" : "-");
	printf((fileStat.st_mode & S_IWGRP) ? "w" : "-");
	printf((fileStat.st_mode & S_IXGRP) ? "x" : "-");
	printf((fileStat.st_mode & S_IROTH) ? "r" : "-");
	printf((fileStat.st_mode & S_IWOTH) ? "w" : "-");
	printf((fileStat.st_mode & S_IXOTH) ? "x" : "-");
	printf(" (%o)\n", fileStat.st_mode & 0777);
	printf("Last modified: %s", ctime(&fileStat.st_mtime));
}

void printFileType(const char *filename) {
	const char *extension = strrchr(filename, '.');
	if (extension != NULL) {
		if (strcmp(extension, ".md") == 0) {
			printf("File Type: Markdown\n");
		} else if (strcmp(extension, ".c") == 0) {
			printf("File Type: C Code\n");
		} else if (strcmp(extension, ".cpp") == 0 || (strcmp(extension, ".cxx")) == 0) {
			printf("File Type: C++ Code\n");
		} else if (strcmp(extension, ".py") == 0) {
			printf("File Type: Python Code\n");
		} else {
			printf("File Type: Unknown\n");
		}
	} else {
		printf("File Type: Unknown\n");
	}
}

static PyObject *gnux_cat(PyObject *self, PyObject *args) {
	const char *filename;
	int status = 0;
	char line[LINE_LENGTH];
	int lineNumber = 1;

	if (!PyArg_ParseTuple(args, "s", &filename)) {
		return NULL;
	}

	FILE *file = fopen(filename, "r");

	if (file == NULL) {
		PyErr_SetString(PyExc_FileNotFoundError, "File not found");
		return NULL;
	}

	while (fgets(line, sizeof(line), file)) {
		printf("%s%3d| %s%s", BLUE_COLOR, lineNumber, RESET_COLOR, line);
		lineNumber++;
	}

	fclose(file);

	printFileDetails(filename);
	printFileType(filename);

	return PyLong_FromLong(status);
}

static PyMethodDef MKDIRMethods[] = { { "gnux_cat", gnux_cat, METH_VARARGS,
										"Create directory (ignore_exists is exist_ok)" },
									  { NULL, NULL, 0, NULL } };

static struct PyModuleDef catmodule = { PyModuleDef_HEAD_INIT, "cat", NULL, -1, MKDIRMethods };

PyMODINIT_FUNC PyInit_cat(void) { return PyModule_Create(&catmodule); }
