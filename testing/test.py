from main.lexer import Lexer
from main.parser import Parser
from main.interpreter import Interpreter
from main.transpiler import LatexTranspiler


if __name__ == "__main__":
    print("=" * 41)
    print("Hello, Alonzo. Your computer is ready.")
    print("Reading input ... ")

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
        input_transpiler = LatexTranspiler(tree)
        input_latex = input_transpiler.transpile()

        res = interpreter.interpret()
        output_transpiler = LatexTranspiler(res)
        output_latex = output_transpiler.transpile()

        print("Input (Latex): ", input_latex)
        print("Result: ", res)
        print("Result (latex): ", output_latex)
