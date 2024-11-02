from main.lexer import Lexer
from main.parser import Parser
from main.interpreter import Interpreter


if __name__ == "__main__":
    print("=" * 41)
    print("Hello, Alonzo. Your computer is ready.")
    print("Reading input ... ")

    # input = open("testing/input.txt", "r").read()
    with open("testing/input.txt", "r") as fid:
        lines = fid.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        print("_________________")
        print("Currently computing: ", line)
        lexer = Lexer(line)
        parser = Parser(lexer)

        tree = parser.parse()

        interpreter = Interpreter(tree)
        res = interpreter.interpret()

        print("Result: ", res)
