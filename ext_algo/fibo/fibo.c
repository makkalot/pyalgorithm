#include <Python.h>

static char fibo_doc[] = "That module is a fibonacci monster";


static PyObject*
fibo_iter(PyObject* self,PyObject *args){

    // the numbers to be added
    PyObject *first_num;
    PyObject *second_num;
    PyObject *tmp_res;

    long int fibo_number,i;

    if (!PyArg_ParseTuple(args, "l", &fibo_number))
             return NULL;


    if(fibo_number == 0 || fibo_number == 1)
        return Py_BuildValue("K",fibo_number);

    //Dont forget to decref ...
    first_num = Py_BuildValue("K",0);
    second_num = Py_BuildValue("K",1);

    //computes the fibo iteratively
    for (i=1;i<fibo_number;i++){
        //we have a new reference
        tmp_res = PyNumber_Add(first_num,second_num);
        
        Py_INCREF(second_num);
        Py_XDECREF(first_num);
        first_num = second_num;
        

        Py_INCREF(tmp_res);
        Py_XDECREF(second_num);
        second_num = tmp_res;

        //give back the reference
        Py_XDECREF(tmp_res);
    }
    Py_XDECREF(first_num);
    return second_num;
}

static PyMethodDef fibo_methods[] = {
        //you list here the methods of that module
        {"iter_fibo", fibo_iter, METH_VARARGS},
        {NULL, NULL}
        };

PyMODINIT_FUNC
initfibo(void){
        //you init here the module ...
        Py_InitModule3("fibo", fibo_methods,fibo_doc);
}

