from . import ast
from . import token
from . import instruction

R_FORMAT = 'R'
I_FORMAT = 'I'

INSTRUCTIONS = set([token.LUI, token.ORI, token.LB, token.PUSH])
REGISTERS = set([
    token.REG0, token.REG1, token.REG2, token.REG3, token.REG4, token.REG5,
    token.REG6, token.REG_ACC
])

INSTRUCTION_FORMAT = {
    token.LUI: I_FORMAT,
    token.ORI: I_FORMAT,
    token.LB: R_FORMAT,
    token.PUSH: R_FORMAT,
}


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer

    def parse_program(self):
        program = ast.Program()

        curr_token = self.lexer.next_token()
        while curr_token.type != token.EOF:
            program.append(self.parse_statement(curr_token))
            curr_token = self.lexer.next_token()

        return program

    def parse_statement(self, instr_token):
        self.assert_token(token.INSTRUCTION, instr_token)

        format = INSTRUCTION_FORMAT.get(instr_token.literal)

        if format == R_FORMAT:
            return self.parse_rformat_statement(instr_token)
        elif format == I_FORMAT:
            return self.parse_iformat_statement(instr_token)
        else:
            raise ParseError("No format exists for {}".format(instr_token))

    def parse_rformat_statement(self, instr_token):
        reg_token = self.lexer.next_token()
        self.assert_token(token.REGISTER, reg_token)
        return ast.RFormatStatement(instr_token, reg_token)

    def parse_iformat_statement(self, instr_token):
        reg_token = self.lexer.next_token()
        self.assert_token(token.REGISTER, reg_token)

        comma_token = self.lexer.next_token()
        self.assert_token_type(token.COMMA, comma_token.type)

        binary_token = self.lexer.next_token()
        self.assert_token(token.BINARY, binary_token)

        return ast.IFormatStatement(instr_token, reg_token, binary_token)

    def assert_token(self, expected_token_type, actual_token):
        self.assert_token_type(expected_token_type, actual_token.type)
        self.assert_token_literal(expected_token_type, actual_token.literal)

    def assert_token_type(self, expectedType, actualType):
        if expectedType != actualType:
            raise ParseError("Expected {}, got {}".format(
                expectedType, actualType))

    def assert_token_literal(self, expected_token_type, token_literal):
        if expected_token_type == token.INSTRUCTION:
            self.assert_instruction(token_literal)
        elif expected_token_type == token.REGISTER:
            self.assert_register(token_literal)
        elif expected_token_type == token.BINARY:
            self.assert_binary(token_literal)

    def assert_instruction(self, token_literal):
        if token_literal not in INSTRUCTIONS:
            raise ParseError(
                "Unknown instruction {}, must be one of {}".format(
                    token_literal, INSTRUCTIONS))

    def assert_register(self, token_literal):
        if token_literal not in REGISTERS:
            raise ParseError("Unknown register {}, must be one of {}".format(
                token_literal, REGISTERS))

    def assert_binary(self, token_literal):
        if len(token_literal[2:]) != 4:
            raise ParseError("Expected a 4-bit binary literal, got {}".format(
                token_literal))


class ParseError(Exception):
    pass
