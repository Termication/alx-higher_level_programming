#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Print information about a Python float object.
 * @p: Pointer to the Python object.
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to the Python object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0, i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = PyBytes_Size(p);
	printf("  size: %zd\n", len);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", len < 10 ? len + 1 : 10);
	while (i < len + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - Print information about a Python list object.
 * @p: Pointer to the Python object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t sz = 0;
	PyObject *it;
	int index = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		sz = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", sz);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (index < sz)
		{
			it = PyList_GET_ITEM(p, index);
			printf("Element %d: %s\n", index, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			else if (PyFloat_Check(it))
				print_python_float(it);
			index++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
