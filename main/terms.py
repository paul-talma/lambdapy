# TODO: use introspection to move methods to Term class
class Term:
    def normal_form(self):
        term = self
        while type(term) is Application and type(term.function) is Abstraction:
            term = term.evaluate()

        return term


class Variable(Term):
    def __init__(self, name: int):
        self.name = name

    # def evaluate(self) -> int:
    #     return self

    def __repr__(self) -> str:
        return f"v_{self.name}"


class Abstraction(Term):
    def __init__(self, var: Variable, expr: Term):
        self.var = var
        self.expr = expr

    # def evaluate(self):
    #     return self

    def __repr__(self) -> str:
        return f"(λ{self.var} . {self.expr})"


class Application(Term):
    def __init__(self, function: Term, argument: Term):
        self.function = function
        self.argument = argument

    # def evaluate(self):
    #     eval_function = self.function.evaluate()
    #     eval_arg = self.argument.evaluate()
    #
    #     if type(eval_function) is Abstraction:
    #         var = eval_function.var
    #         expr = eval_function.expr
    #         res = substitute(expr, var, eval_arg)
    #     else:
    #         res = Application(eval_function, eval_arg)
    #
    #     return res

    def __repr__(self) -> str:
        return f"({self.function} {self.argument})"


# TODO: move to Term class? kinda hard since need to return self instance.
def substitute(formula: Term, x: Variable, term: Term) -> Term:
    """
    recursively substitute term for x in formula
    """
    if type(formula) is Variable:
        return term if formula.name == x.name else formula

    if type(formula) is Abstraction:
        var = formula.var
        expr = formula.expr

        # x is bound by the lambda
        if var.name == x.name:
            return formula

        # x is in FV(formula) and var is in FV(term)
        # need to find a fresh variable and substitute to avoid clash
        if x in free_variables(formula) and formula.var in free_variables(term):
            vars = free_variables(formula).union(free_variables(term))
            z = find_fresh_fv(vars)
            res = Abstraction(z, substitute(substitute(formula, var, z), x, term))
            return res

        # x is not free in formula, or var is not free in term
        expr = substitute(expr, x, term)
        res = Abstraction(var, expr)
        return res

    if type(formula) is Application:
        function = formula.function
        argument = formula.argument
        return Application(substitute(function, x, term), substitute(argument, x, term))


def free_variables(expr: Term) -> set[Variable]:
    """
    recursively compute the free variables of expr
    """
    if type(expr) is Variable:
        return {expr}

    if type(expr) is Abstraction:
        var = expr.var
        expr = expr.expr
        free_vars = free_variables(expr)
        if var in free_vars:
            free_vars.remove(var)

        return free_vars

    if type(expr) is Application:
        function = expr.function
        argument = expr.argument
        free_vars = free_variables(function).union(free_variables(argument))
        return free_vars


def find_fresh_fv(vars: set[Variable]) -> Variable:
    """
    return the variable with lowest index not in vars
    """
    length = vars.size()
    indices = [var.name for var in vars]
    for i in range(length + 1):
        if i not in indices:
            return Variable(i)
