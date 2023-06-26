#define Py_BUILD_CORE

#include <stdio.h>
#include <python3.8/Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: A pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");
	for (i = 0; i <= size && i < 10; i++)
		printf("%02hhx%c", str[i], i < 9 ? ' ' : '\n');
}

/**
 * print_python_float - Prints some basic info about Python floats
 * @p: A pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *str;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = PyFloat_AsDouble(p);
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
