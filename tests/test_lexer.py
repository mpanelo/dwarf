import unittest
from dwarf.lexer import Lexer
from dwarf.ioreader import IOReader
from dwarf import token


class LexerTestCase(unittest.TestCase):

    def setUp(self):
        content = """
            push $r2
            %
            lui 0b0000
            add $r3, $r2, $r1
        """.strip()
        ioreader = IOReader(content)
        self.lexer = Lexer(ioreader)

    def test_next_token(self):
        expected_tokens = [
            token.Token(token.INSTRUCTION, token.PUSH),
            token.Token(token.REGISTER, token.REG2),
            token.Token(token.ILLEGAL, '%'),
            token.Token(token.INSTRUCTION, token.LUI),
            token.Token(token.BINARY, '0b0000'),
            token.Token(token.INSTRUCTION, token.ADD),
            token.Token(token.REGISTER, token.REG3),
            token.Token(token.COMMA, ','),
            token.Token(token.REGISTER, token.REG2),
            token.Token(token.COMMA, ','),
            token.Token(token.REGISTER, token.REG1),
            token.Token(token.EOF, 'EOF')
        ]

        for expected_token in expected_tokens:
            self.assertEqual(expected_token, self.lexer.next_token())
