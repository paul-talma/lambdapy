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
        self.visit(self.tree)

    def visit_Variable(self, variable):
        pass

    def visit_Abstraction(self, abstraction):
        pass

    def visit_Application(self, application):
        pass
