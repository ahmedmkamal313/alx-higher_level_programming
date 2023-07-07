#include <Python.h>

/**
 * print_python_string - Prints a Python string.
 *
 * @param p: The Python string to print.
 */
void print_python_string(PyObject *p) 
{
	if (!PyString_Check(p)) 
	{
		fprintf(stderr, "p is not a valid string\n");
		return;
	}

	char *str = PyString_AsString(p);
	printf("The Python string is: \"%s\"\n", str);
}
