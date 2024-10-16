from main.terms import Variable, Abstraction, Application
from main.lexer import TokenTypes


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = lexer.get_token()

    def error(self, type):
        raise Exception(
            f"Parser error. Expected type {type} but got Token: {self.token}"
        )

    def eat(self, type):
        if self.token.type == type:
            self.token = self.lexer.get_token()
        else:
            self.error(type)

    def expression(self):
        if self.token.type == TokenTypes.VAR:
            var = self.variable()
            return var

        elif self.token.type == TokenTypes.LAMBDA:
            return self.abstraction()

        return self.application()

    # TODO: need to process var.value into a number
    # var.value is a string, e.g. "x2"
    # need to extract the 2
    def variable(self):
        var_token = self.token
        num = self.extract_num(var_token)
        self.eat(TokenTypes.VAR)
        return Variable(num)

    # WARN: this solution is probably unstable
    # WARN: does not account for different prefixes e.g. x1 != y1
    def extract_num(self, var_token):
        val = var_token.value
        return int(val[1:])

    def abstraction(self):
        self.eat(TokenTypes.LAMBDA)
        var = self.variable()
        self.eat(TokenTypes.DOT)
        expr = self.expression()
        return Abstraction(var, expr)

    def application(self):
        self.eat(TokenTypes.LPAR)
        expr1 = self.expression()
        expr2 = self.expression()
        self.eat(TokenTypes.RPAR)
        return Application(expr1, expr2)

    def parse(self):
        tree = self.expression()
        if self.token.type != TokenTypes.EOS:
            self.error()
        return tree
