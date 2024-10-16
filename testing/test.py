from main.lexer import Lexer
from main.parser import Parser


if __name__ == "__main__":
    print("=" * 41)
    print("Hello, Alonzo. Your computer is ready.")
    print("Reading input ... ")

    input = open("testing/input.txt", "r").read()

    lexer = Lexer(input)
    parser = Parser(lexer)

    tree = parser.parse()
    print(tree)
    print(tree.var, tree.expr)
