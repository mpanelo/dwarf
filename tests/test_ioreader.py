import unittest
from dwarf.lex.ioreader import IOReader


class IOReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.content = """
            lui $r1, 0b1000
            lb $r0
            add $r2, $r1, $r0
        """.strip()
        self.ioreader = IOReader(self.content)

    def test_end_of_file(self):
        for i in range(len(self.content)):
            self.ioreader.read_char()
        self.assertTrue(self.ioreader.end_of_file())

    def test_char(self):
        expected_char = self.content[0]
        self.assertEqual(expected_char, self.ioreader.char())

    def test_peek_char(self):
        expected_char = self.content[1]
        actual_char = self.ioreader.peek_char()
        self.assertEqual(expected_char, actual_char)

    def test_read_char(self):
        expected_char = self.content[3]

        for i in range(3):
            self.ioreader.read_char()

        self.assertEqual(expected_char, self.ioreader.char())
