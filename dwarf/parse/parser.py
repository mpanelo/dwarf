from dwarf.lex import token
from dwarf.parse import ast
from dwarf.parse.error import ParseError
from dwarf.parse import assertor

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
        assertor.assert_instruction(instr_token)

        if instr_token.literal in FORMAT_R:
            return self.parse_r_instruction(instr_token)
        if instr_token.literal in FORMAT_I:
            return self.parse_i_instruction(instr_token)

        raise ParseError("No format exists for {}".format(instr_token))

    def parse_r_instruction(self, instr_token):
        reg_token = self.lexer.next_token()
        assertor.assert_register(reg_token)
        return ast.RTypeInstruction(instr_token, reg_token)

    def parse_i_instruction(self, instr_token):
        bin_token = self.lexer.next_token()
        assertor.assert_binary(bin_token)
        return ast.ITypeInstruction(instr_token, bin_token)
