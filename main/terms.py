# these classes define the nodes in the AST


class Term:
    def normal_form(self):
        term = self
        while type(term) is Application and type(term.function) is Abstraction:
            term = term.evaluate()

        return term


class Variable(Term):
    def __init__(self, name: int):
        self.name = name

    def __repr__(self) -> str:
        return f"v_{self.name}"


class Abstraction(Term):
    def __init__(self, var: Variable, expr: Term):
        self.var = var
        self.expr = expr

    def __repr__(self) -> str:
        return f"(λ{self.var} . {self.expr})"


class Application(Term):
    def __init__(self, function: Term, argument: Term):
        self.function = function
        self.argument = argument

    def __repr__(self) -> str:
        return f"({self.function} {self.argument})"
