from . import ast
from . import token
from . import instruction

R_FORMAT = 'R'
I_FORMAT = 'I'

INSTRUCTIONS = set([token.LUI, token.ORI, token.LB])
REGISTERS = set([
    token.REG0, token.REG1, token.REG2, token.REG3, token.REG4, token.REG5,
    token.REG6, token.REG_ACC
])

INSTRUCTION_FORMAT = {
    token.LUI: I_FORMAT,
    token.ORI: I_FORMAT,
    token.LB: R_FORMAT,
}


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.peek_token = self.lexer.next_token()
        self.next_token()

    def parse_program(self):
        program = ast.Program()

        while self.curr_token.type != token.EOF:
            program.append(self.parse_statement())
            self.next_token()

        return program

    def parse_statement(self):
        if self.curr_token.type != token.INSTRUCTION:
            raise ParseError("Statement must begin with an instruction")
        if self.curr_token.literal not in INSTRUCTIONS:
            raise ParserError("Invalid instruction {}".format(
                self.curr_token.literal))

        format = INSTRUCTION_FORMAT.get(self.curr_token.literal)

        if format == R_FORMAT:
            return self.parse_rformat_statement()
        elif format == I_FORMAT:
            return self.parse_iformat_statement()
        else:
            raise ParseError("No format exists for {}".format(self.curr_token))

    def parse_rformat_statement(self):
        instr_token = self.curr_token
        self.next_token()

        if self.curr_token.type != token.REGISTER:
            raise ParseError(
                "{} must be followed by a register".format(instr_token))
        if self.curr_token.literal not in REGISTERS:
            raise ParseError("Invalid register {}".format(
                self.curr_token.literal))

        return ast.RFormatStatement(instr_token, self.curr_token)

    def parse_iformat_statement(self):
        instr_token = self.curr_token
        self.next_token()

        if self.curr_token.type != token.REGISTER:
            raise ParseError(
                "{} must be followed by a register".format(instr_token))
        if self.curr_token.literal not in REGISTERS:
            raise ParseError("Invalid register {}".format(
                self.curr_token.literal))

        reg_token = self.curr_token
        self.next_token()

        if self.curr_token.type != token.COMMA:
            raise ParseError("Expected ',' after {}".format(reg_token))

        self.next_token()

        if self.curr_token.type != token.BINARY:
            raise ParseError(
                "{} must be followed by a binary".format(reg_token))
        if len(self.curr_token.literal[2:]) != 4:
            raise ParseError("Invalid binary {}".format(
                self.curr_token.literal))

        return ast.IFormatStatement(instr_token, reg_token, self.curr_token)

    def next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.next_token()


class ParseError(Exception):
    pass
