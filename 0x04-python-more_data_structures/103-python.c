#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 *
 * @p: PyObject representing a Python bytes object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *data_ptr;
	long int data_size, idx, limit_size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data_size = ((PyVarObject *)(p))->ob_size;
	data_ptr = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", data_size);
	printf("  trying string: %s\n", data_ptr);

	if (data_size >= 10)
		limit_size = 10;
	else
		limit_size = data_size + 1;

	printf("  first %ld bytes:", limit_size);

	for (idx = 0; idx < limit_size; idx++)
		if (data_ptr[idx] >= 0)
			printf(" %02x", data_ptr[idx]);
		else
			printf(" %02x", 256 + data_ptr[idx]);

	printf("\n");
}
/**
 * print_python_list - Prints information about a Python list object
 *
 * @p: PyObject representing a Python list object
 * Return: void
 */

void print_python_list(PyObject *p)
{
	long int list_size, idx;
	PyListObject *list_obj;
	PyObject *list_item;

	list_size = ((PyVarObject *)(p))->ob_size;
	list_obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		list_item = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((list_item)->ob_type)->tp_name);
		if (PyBytes_Check(list_item))
			print_python_bytes(list_item);
	}
}
