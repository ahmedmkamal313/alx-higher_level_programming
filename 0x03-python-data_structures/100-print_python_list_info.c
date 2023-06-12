#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a Python object (list)
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *item;

	/* Check if p is a list object */
	if (!PyList_Check(p))
		return;

	/* Cast p to a list object */
	list = (PyListObject *)p;

	/* Get the size of the list */
	size = PyList_Size(p);

	/* Print the size and the allocated space of the list */
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	/* Loop through list and print type and reference count of each element */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i); /* Get the item at index i */
		printf("Element %ld: %s\n", i, item->ob_type->tp_name); /* Print type name */
		printf("  refcount: %ld\n", item->ob_refcnt); /* Print the reference count */
	}
}
