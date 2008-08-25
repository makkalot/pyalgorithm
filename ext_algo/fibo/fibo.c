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

    //printf("\nThe value to compute is %ld",fibo_number);

    if(fibo_number == 0 || fibo_number == 1)
        return Py_BuildValue("l",fibo_number);

    //Dont forget to decref ...
    first_num = Py_BuildValue("l",0);
    second_num = Py_BuildValue("l",1);

    //PyObject_Print(first_num, stdout, 0);
    //printf("\n\n");
    //PyObject_Print(second_num, stdout, 0);
    //printf("\n\n");

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

long int r_fib(long int f_num){
    // A recursive implementation for that

    if(f_num == 0 || f_num == 1)
        return f_num;

    return r_fib(f_num-1) + r_fib(f_num-2);
}

static PyObject*
fibo_rec(PyObject* self,PyObject *args){
     
    long int fibo_number,result;

    if (!PyArg_ParseTuple(args, "l", &fibo_number))
             return NULL;

    result = r_fib(fibo_number);
    return Py_BuildValue("l",result);
 
}



static PyMethodDef fibo_methods[] = {
        //you list here the methods of that module
        {"iter_fibo", fibo_iter, METH_VARARGS},
        {"rec_fibo", fibo_rec, METH_VARARGS},
        {NULL, NULL}
        };

PyMODINIT_FUNC
initfibo(void){
        //you init here the module ...
        Py_InitModule3("fibo", fibo_methods,fibo_doc);
}

