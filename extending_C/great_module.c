// great_module.c

// 引用python的標頭檔案
#include <Python.h>

int great_function(int a) {
    return a + 1;
}

// 包裹函式，用來包裹需要轉化為python的函式，在方法前面加下劃線。
static PyObject * _great_function(PyObject *self, PyObject *args)
{
    int _a;
    int res;

    // 檢查引數型別是否正確，python引數轉化為c
    if (!PyArg_ParseTuple(args, "i", &_a))
        return NULL;
    res = great_function(_a);
    return PyLong_FromLong(res);
}

// 定義的方法表，用於在python中查詢
static PyMethodDef GreateModuleMethods[] = {
    {
        "great_function",
        _great_function,
        METH_VARARGS,
        ""
    },
    {NULL, NULL, 0, NULL}
};

// 必須以module名前面加init定義該方法
PyMODINIT_FUNC initgreat_module(void) {
    (void) Py_InitModule("great_module", GreateModuleMethods);
}
