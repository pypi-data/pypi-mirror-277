/**
* =============================================================================
* muparser
* Copyright(C) 2018 Ayuto. All rights reserved.
* =============================================================================
*
* This program is free software; you can redistribute it and/or modify it under
* the terms of the GNU General Public License, version 3.0, as published by the
* Free Software Foundation.
*
* This program is distributed in the hope that it will be useful, but WITHOUT
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
* FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
* details.
*
* You should have received a copy of the GNU General Public License along with
* this program.  If not, see <http://www.gnu.org/licenses/>.
**/

// ============================================================================
// >> INCLUDES
// ============================================================================
// Python
#include "Python.h"

// C/C++
#include <stdio.h>
#include <list>

// MuParser
#include "muParser.h"
using namespace mu;


// ============================================================================
// >> GLOBAL VARIABLES
// ============================================================================
mu::Parser g_MathParser;

// A Python callback for variable parsing
PyObject* g_pParseVarCallback;

std::list<double*> g_Variables;


// ============================================================================
// >> CALLBACKS
// ============================================================================
double NotParserCallback(double val)
{
    return !val;
}

double* ParseVarCallback(const char* szName, void* a_pUserData)
{
    static double zero = 0.0;
    
    PyObject* pResult = PyObject_CallFunction(g_pParseVarCallback, "s", szName);
    if (!pResult)
        return &zero;
    
    double* pVar = (double*) malloc(sizeof(double));
    *pVar = PyFloat_AsDouble(pResult);
    Py_XDECREF(pResult);
    g_Variables.push_back(pVar);
    return pVar;
}


// ============================================================================
// >> EXPORTED FUNCTIONS
// ============================================================================
static PyObject* init_parser(PyObject* self, PyObject* args)
{
    PyObject* pTempCallback = NULL;
    if (!PyArg_ParseTuple(args, "O", &pTempCallback))
        return NULL;
        
    if (!PyCallable_Check(pTempCallback)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be callable.");
        return NULL;
    }
    
    Py_XINCREF(pTempCallback);              // Add a reference to new callback
    Py_XDECREF(g_pParseVarCallback);        // Dispose of previous callback
    g_pParseVarCallback = pTempCallback;    // Remember new callback
    
    g_MathParser.DefineInfixOprt("!", &NotParserCallback);
    g_MathParser.SetVarFactory(&ParseVarCallback, &g_MathParser);
    g_MathParser.EnableOptimizer();
    
    Py_RETURN_NONE;
}

static PyObject* unload_parser(PyObject* self, PyObject* args)
{
    Py_XDECREF(g_pParseVarCallback);
    g_pParseVarCallback = NULL;
    Py_RETURN_NONE;
}

static PyObject* clear_vars(PyObject* self, PyObject* args)
{
    g_MathParser.ClearVar();
    for (std::list<double*>::iterator it=g_Variables.begin(); it != g_Variables.end(); ++it)
        free(*it);
    
    g_Variables.clear();
    Py_RETURN_NONE;
}

static PyObject* parse_expr(PyObject* self, PyObject* args)
{
    char* expr = NULL;
    if (!PyArg_ParseTuple(args, "s", &expr))
        return NULL;
    
    if (!g_pParseVarCallback) {
        PyErr_SetString(PyExc_RuntimeError, "Parse variable callback not yet defined.");
        return NULL;
    }
    
    try {
        g_MathParser.SetExpr(expr);
        return Py_BuildValue("d", g_MathParser.Eval());
    }
    catch (Parser::exception_type &e)
    {
        PyErr_SetString(PyExc_RuntimeError, e.GetMsg().c_str());
        return NULL;
    }
    Py_RETURN_NONE;
}


// ============================================================================
// >> GLOBAL VARIABLES
// ============================================================================
static PyMethodDef g_PyFuncs[] = {
    {"init_parser",  init_parser, METH_VARARGS, "Initialize MuParser."},
    {"unload_parser",  unload_parser, METH_VARARGS, "Unload MuParser."},
    {"clear_vars",  clear_vars, METH_VARARGS, "Clear variables."},
    {"parse_expr",  parse_expr, METH_VARARGS, "Parse an expression."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef muparsermodule = {
   PyModuleDef_HEAD_INIT,
   "muparser",
   NULL,
   -1,
   g_PyFuncs
};

// ============================================================================
// >> INITIALIZATION FUNCTION
// ============================================================================
PyMODINIT_FUNC PyInit_muparser(void)
{
    return PyModule_Create(&muparsermodule);
}