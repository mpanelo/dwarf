from dwarf.lex import token
from dwarf.parse import ast

INSTRUCTIONS = set([token.LUI, token.ORI, token.LB,
                    token.PUSH, token.SB, token.ADD])
REGISTERS = set([
    token.REG0, token.REG1, token.REG2, token.REG3, token.REG4, token.REG5,
    token.REG6, token.REG7
])

FORMAT_I = set([
    token.LUI,
    token.ORI,
])

FORMAT_R = set([
    token.LB,
    token.PUSH,
    token.ADD,
    token.SB,
])


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer

    def parse_program(self):
        program = ast.Program()

        curr_token = self.lexer.next_token()
        while curr_token.type != token.EOF:
            program.append(self.parse_instruction(curr_token))
            curr_token = self.lexer.next_token()

        return program

    def parse_instruction(self, instr_token):
        self.assert_token(token.INSTRUCTION, instr_token)

        if instr_token.literal in FORMAT_R:
            return self.parse_r_instruction(instr_token)
        if instr_token.literal in FORMAT_I:
            return self.parse_i_instruction(instr_token)

        raise ParseError("No format exists for {}".format(instr_token))

    def parse_r_instruction(self, instr_token):
        reg_token = self.lexer.next_token()
        self.assert_token(token.REGISTER, reg_token)
        return ast.RTypeInstruction(instr_token, reg_token)

    def parse_i_instruction(self, instr_token):
        binary_token = self.lexer.next_token()
        self.assert_token(token.BINARY, binary_token)
        return ast.ITypeInstruction(instr_token, binary_token)

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
