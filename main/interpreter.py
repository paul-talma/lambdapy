from main.terms import Abstraction, Application, Variable, Term


def find_fresh_fv(vars: set[Variable]) -> Variable:
    """
    return the variable with lowest index not in vars
    """
    length = vars.size()
    indices = [var.name for var in vars]
    for i in range(length + 1):
        if i not in indices:
            return Variable(i)


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


def substitute(formula: Term, x: Variable, term: Term) -> Term:
    """
    recursively substitute term for x in formula
    """
    t = type(formula)

    # if formula is a variable y, sub only if x == y
    if t is Variable:
        return term if formula.name == x.name else formula

    # if formula is lambda var . expr, we want to substitute term for x in
    # var and expr. However, we must be careful to avoid clas of variables.
    if t is Abstraction:
        var = formula.var
        expr = formula.expr

        # x is bound
        if var.name == x.name:
            return formula

        # x is in FV(formula) and var is in FV(term)
        # need to find a fresh variable and substitute to avoid clash
        form_fvs = free_variables(formula)
        term_fvs = free_variables(term)
        if x in form_fvs and var in term_fvs:
            fvs = form_fvs.union(term_fvs)
            z = find_fresh_fv(fvs)
            sub1 = substitute(formula, var, z)
            sub2 = substitute(sub1, x, term)
            res = Abstraction(z, sub2)
            return res

        # x is not free in formuls, or var is not free in term
        expr = substitute(expr, x, term)
        res = Abstraction(var, expr)
        return res

    # if formula is MN, we substitute term for x in M and N separately
    if t is Application:
        func = formula.function
        arg = formula.argument
        sub1 = substitute(func, x, term)
        sub2 = substitute(arg, x, term)
        res = Application(sub1, sub2)
        return res


class NodeVisitor:
    def visit(self, node):
        name = "visit_" + type(node).__name__
        visitor = getattr(self, name, self.default_visitor)
        return visitor(node)

    def default_visitor(self, node):
        raise Exception(f"No method named visit_{type(node).__name__}.")


class Interpreter(NodeVisitor):
    def __init__(self, tree):
        self.tree = tree

    def interpret(self):
        if self.tree is None:
            return ""
        return self.visit(self.tree)

    def visit_Variable(self, variable):
        return variable

    def visit_Abstraction(self, abstraction):
        return abstraction

    def visit_Application(self, application):
        func = application.function
        if type(func) is Abstraction:
            var = func.var
            expr = func.expr
            arg = application.argument
            # arg = self.visit(application.argument)
            res = substitute(expr, var, arg)
            res = self.visit(res)
            return res
