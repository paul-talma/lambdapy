from dataclasses import dataclass


@dataclass
class TokenTypes:
    LAMBDA = "LAMBDA"
    LPAR = "LPAR"
    RPAR = "RPAR"
    DOT = "DOT"
    VAR = "VAR"
    EOS = "EOS"


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Type: {self.type}, value: {self.value}"

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.max_len = len(input)
        self.char = input[0]

    def advance(self):
        self.pos += 1
        if self.pos < self.max_len:
            self.char = self.input[self.pos]
        else:
            self.char = None

    def skip_spaces(self):
        while self.char is not None and self.char.isspace():
            self.advance()

    def error(self):
        raise Exception("Lexer error.")

    def check_lambda(self):
        curr_word = ""
        temp_char = self.char
        temp_pos = self.pos
        while temp_char.isalpha():
            curr_word += temp_char
            temp_pos += 1
            if temp_pos < self.max_len:
                temp_char = self.input[temp_pos]
            else:
                temp_char = None
        if curr_word == "lambda":
            return True
        return False

    def get_var(self):
        var_name = ""
        while self.char is not None and self.char.isalnum():
            var_name += self.char
            self.advance()
        return Token(TokenTypes.VAR, var_name)

    def get_token(self):
        if self.pos >= self.max_len:
            return Token(TokenTypes.EOS, None)

        if self.char.isspace():
            self.skip_spaces()
            return self.get_token()

        if self.char == "\\":
            self.advance()
            return Token(TokenTypes.LAMBDA, "\\")

        if self.char == "(":
            self.advance()
            return Token(TokenTypes.LPAR, "(")

        if self.char == ")":
            self.advance()
            return Token(TokenTypes.RPAR, ")")

        if self.char == ".":
            self.advance()
            return Token(TokenTypes.DOT, ".")

        if self.char.isalpha():
            if self.check_lambda():
                token = Token(TokenTypes.LAMBDA, "lambda")
            token = self.get_var()
            return token
