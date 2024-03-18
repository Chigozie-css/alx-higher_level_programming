#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints information about PyFloatObject
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	double value = 0;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %.17g\n", value);
}

/**
 * print_python_bytes - prints information about PyBytesObject
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (Py_ssize_t i = 0; i < size + 1 && i < 10; ++i)
		printf(" %02hhx", string[i]);
	printf("\n");
}

/**
 * print_python_list - prints information about PyListObject
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (Py_ssize_t i = 0; i < size; ++i)
		{
			PyObject *item = PyList_GET_ITEM(p, i);

			printf("Element %zd: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
