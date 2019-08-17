from dwarf.lex import token
from dwarf.parser.error import ParseError


INSTRUCTIONS = set(
    [token.LUI, token.ORI, token.LB, token.PUSH, token.SB, token.ADD])

REGISTERS = set([
    token.REG0, token.REG1, token.REG2, token.REG3, token.REG4, token.REG5,
    token.REG6, token.REG7
])


def assert_binary(tok):
    _assert_token_type(token.BINARY, tok.type)

    binary = tok.literal[2:]
    bits = [bit for bit in binary if bit == '0' or bit == '1']

    if len(bits) != len(binary):
        raise ParseError('{} is not a binary literal'.format(binary))
    if len(bits) != 4:
        raise ParseError('Expected 4-bit binary literal')


def assert_instruction(tok):
    _assert_token_type(token.INSTRUCTION, tok.type)

    if tok.literal not in INSTRUCTIONS:
        raise ParseError("Invalid instruction '{}'".format(tok.literal))


def assert_register(tok):
    _assert_token_type(token.REGISTER, tok.type)

    if tok.literal not in REGISTERS:
        raise ParseError("Invalid register '{}'".format(tok.literal))


def _assert_token_type(expected, actual):
    if expected != actual:
        err = 'Expected {}, received {}'.format(expected, actual)
        raise ParseError(err)
