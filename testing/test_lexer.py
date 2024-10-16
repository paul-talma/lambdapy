from lexer import Lexer


if __name__ == "__main__":
    print("=" * 41)
    print("Hello, Alonzo. Your computer is ready.")
    print("Reading input ... ")

    input = open("testing/input.txt", "r").read()

    lexer = Lexer(input)
    token = lexer.get_token()
    print(f"token: {token}, char = {lexer.char}")
    token = lexer.get_token()
    print(f"token: {token}, char = {lexer.char}")
    token = lexer.get_token()
    print(f"token: {token}, char = {lexer.char}")
    token = lexer.get_token()
    print(f"token: {token}, char = {lexer.char}")
