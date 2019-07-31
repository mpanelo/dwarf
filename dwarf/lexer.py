from . import token


class Lexer(object):
    def __init__(self, ioreader):
        self.ioreader = ioreader

    def next_token(self):
        self.skip_whitespace()

        if self.ioreader.char() == '$':
            tok = token.Token(token.REGISTER, self.read())
        elif self.ioreader.char() == '0' and self.ioreader.peek_char() == 'b':
            tok = token.Token(token.BINARY, self.read())
        elif self.ioreader.char() == ',':
            tok = token.Token(token.COMMA, self.ioreader.char())
            self.ioreader.read_char()
        elif self.ioreader.end_of_file():
            tok = token.Token(token.EOF, self.ioreader.char())
        elif self.ioreader.char().isalpha():
            tok = self.instruction_token()
        else:
            tok = token.Token(token.ILLEGAL, self.ioreader.char())
            self.ioreader.read_char()

        return tok

    def skip_whitespace(self):
        while self.ioreader.char().isspace():
            self.ioreader.read_char()

    def instruction_token(self):
        instr = self.read()
        return token.Token(token.INSTRUCTION, instr)

    def read(self):
        instr = ''

        while self._is_valid_instr_char():
            instr += self.ioreader.char()
            self.ioreader.read_char()

        # TODO validate that instr is actually an instruction
        return instr

    def _is_valid_instr_char(self):
        return not (self.ioreader.char().isspace() or
                    self.ioreader.end_of_file() or self.ioreader.char() == ',')
