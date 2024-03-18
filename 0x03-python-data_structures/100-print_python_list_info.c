#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information
 * about a Python list
 * @p: Pointer to the PyObject representing the list
 *
 * Description:
 *   This function prints the size of a Python
 *   list and information about each element
 *   within the list.
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = PyList_Size(p);
	int index;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (index = 0; index < list_size; index++)
		printf("Element %i: %s\n", index, Py_TYPE(obj->ob_item[index])->tp_name);
}
