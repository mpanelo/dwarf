from . import token


class Lexer(object):
    def __init__(self, ioreader):
        self.ioreader = ioreader

    def next_token(self):
        self._skip_whitespace()

        if self.ioreader.char() == '$':
            tok = token.Token(token.REGISTER, self._read())
        elif self.ioreader.char() == '0' and self.ioreader.peek_char() == 'b':
            tok = token.Token(token.BINARY, self._read())
        elif self.ioreader.char() == ',':
            tok = token.Token(token.COMMA, self.ioreader.char())
            self.ioreader.read_char()
        elif self.ioreader.end_of_file():
            tok = token.Token(token.EOF, self.ioreader.char())
        elif self.ioreader.char().isalpha():
            tok = self._instruction_token()
        else:
            tok = token.Token(token.ILLEGAL, self.ioreader.char())
            self.ioreader.read_char()

        return tok

    def _skip_whitespace(self):
        while self.ioreader.char().isspace():
            self.ioreader.read_char()

    def _instruction_token(self):
        instr = self._read()
        return token.Token(token.INSTRUCTION, instr)

    def _read(self):
        instr = ''

        while self._can_consume_char():
            instr += self.ioreader.char()
            self.ioreader.read_char()

        # TODO validate that instr is actually an instruction
        return instr

    def _can_consume_char(self):
        current_char = self.ioreader.char()
        return not (current_char.isspace()
                    or current_char == ','
                    or self.ioreader.end_of_file())
