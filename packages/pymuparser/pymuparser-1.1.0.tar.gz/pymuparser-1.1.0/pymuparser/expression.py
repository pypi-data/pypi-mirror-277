import numpy as np
import muparser
from copy import copy
import re


class ScalarExpression(object):
    def __init__(self, expression, variables, constants=None, extra_functions=None):
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

        self.extra_functions = False
        if extra_functions is None:
            self.expr = expression + " "
        else:
            self.extra_functions = True
            self._process_subexpressions(expression + " ", variables, constants, extra_functions)

    def _process_subexpressions(self, expr, variables, constants, extra_functions):
        j = 0
        k = 0
        brackets = []
        open_brackets = []
        for i, char in enumerate(expr):
            if char == "(":
                brackets.append([k, i])
                open_brackets.append(j)
                j += 1
                k += 1
            if char == ")":
                brackets[open_brackets[-1]].append(i)
                del open_brackets[-1]
                k -= 1
        brackets = np.array(brackets, dtype=int)

        # positions provides the
        # nesting level, function index, and the indices of the function start,
        # open bracket and close bracket
        positions = [[*brackets[np.argwhere(brackets == m.end())[0][0]], i, m.start()]
                     for i, func in enumerate(extra_functions)
                     for m in re.finditer(func[0], expr)]
        
        # Reinit if positions is empty
        if len(positions) == 0:
            self.__init__(expr, variables, constants, None)
            return

        positions = np.array(positions, dtype=int)[:, [0, 3, 4, 1, 2]]
        positions = positions[positions[:, 0].argsort()[::-1]]

        replacement_positions = copy(positions)
        replacement_expr = copy(expr)
        replacement_variables = copy(variables)
        self.subexpressions = []

        for i in range(len(replacement_positions)):
            pos = replacement_positions[i]
            full_subexpr = replacement_expr[pos[2]:pos[4]+1]
            replacement_subexpr = f"subexpr_{i}"
            subexpr = copy(replacement_expr[pos[3]:pos[4]+1])
            subexpr = ScalarExpression(subexpr,
                                       copy(replacement_variables), constants)
            func = extra_functions[pos[1]][1]
            self.subexpressions.append([replacement_subexpr, func, subexpr])

            # now modify the expression by
            # 1) replacing the subexpression with the new variable
            delta_len = len(replacement_subexpr) - len(full_subexpr)
            replacement_expr = f"{replacement_expr[0:pos[2]]}{replacement_subexpr}{replacement_expr[pos[4]+1:]}" 

            # 2) add the variable to replacement_variables
            replacement_variables.append(replacement_subexpr)

            # 3) modify the positions array to account for the length change
            # of the expression
            for j in range(i+1, len(replacement_positions)):
                for k in range(2, 5):
                    if replacement_positions[j][k] > pos[2]:
                        replacement_positions[j][k] += delta_len

            self.master_function = ScalarExpression(replacement_expr, replacement_variables, constants)

    def _parse_var(self, name):
        idx = self.variables.index(name)
        return self._values[idx]

    def evaluate(self, values):
        if self.n_variables != values.shape[-1]:
            raise Exception(f"Number of variables ({self.n_variables}) is not the same as the number of values ({values.shape[-1]}). Did you forget to set a variable, or pass too many variable values to evaluate?")
        if self.extra_functions:
            values_c = copy(values)
            for subexpression in self.subexpressions:
                subexpr_values = subexpression[2].evaluate(values_c)
                variable_values = subexpression[1](subexpr_values)
                values_c = np.concatenate((values_c, np.expand_dims(variable_values, -1)), axis=-1)
            return self.master_function.evaluate(values_c)
        else:
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
    def __init__(self, expression, variables, constants=None, extra_functions=None):
        list_expressions = expression.split(";")
        self.scalar_expressions = [ScalarExpression(expression, variables, constants, extra_functions)
                                   for expression in list_expressions]
        self.variables = self.scalar_expressions[0].variables
        self.n_variables = self.scalar_expressions[0].n_variables
        self.n_constants = self.scalar_expressions[0].n_constants

    def evaluate(self, values):
        return np.array([expr.evaluate(values) for expr in self.scalar_expressions])
