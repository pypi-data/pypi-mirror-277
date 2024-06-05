import numpy as np
import muparser
from copy import copy


class ScalarExpression(object):
    def __init__(self, expression, variables, constants=None):
        self.variables = copy(variables)
        self.n_variables = len(variables)
        self._values = [np.nan for i in range(len(self.variables))]

        self.n_constants = 0
        if constants is not None:
            self.n_constants = len(constants)
            for i, (key, value) in enumerate(constants.items()):
                self.variables.append(key)
                self._values.append(value)

        self._values = np.array(self._values)
        self.expr = expression + " "

    def _parse_var(self, name):
        idx = self.variables.index(name)
        return self._values[idx]

    def evaluate(self, values):
        muparser.init_parser(self._parse_var)
        if len(values.shape) == 1:
            self._values[:self.n_variables] = values
            muparser.clear_vars()
            return muparser.parse_expr(self.expr)
        else:
            y = np.empty(values.shape[:-1])

            for i in np.ndindex(values.shape[:-1]):
                self._values[:self.n_variables] = values[i]
                muparser.clear_vars()
                y[i] = muparser.parse_expr(self.expr)
            return y


class VectorExpression(object):
    def __init__(self, expression, variables, constants=None):
        list_expressions = expression.split(";")
        self.scalar_expressions = [ScalarExpression(expression, variables, constants)
                                   for expression in list_expressions]
        self.variables = self.scalar_expressions[0].variables
        self.n_variables = self.scalar_expressions[0].n_variables
        self.n_constants = self.scalar_expressions[0].n_constants

    def evaluate(self, values):
        return np.array([expr.evaluate(values) for expr in self.scalar_expressions])
