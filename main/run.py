from main.lexer import Lexer
from main.parser import Parser
from main.interpreter import Interpreter


def interpret(text: str):
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    res = interpreter.interpret()
    return res.__repr__()
