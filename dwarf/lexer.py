from . import token
from .file import File

class Lexer(object):

	def __init__(self, file):
		self.file = file

	def tokenize(self):
		tokens = []

		while not self.file.is_closed():
			token = self.next_token()
			print(token)
			tokens.append(token)

		return tokens

	def next_token(self):
		self.skip_whitespace()

		if self.file.char() == '$':
			tok = token.Token(token.REGISTER, self.read())
		elif self.file.char() == '0' and self.file.peek_char() == 'b':
			tok = token.Token(token.BINARY, self.read())
		elif self.file.char() == ',':
			tok = token.Token(token.COMMA, self.file.char())
			self.file.read_char()
		elif self.file.char() == File.EOF:
			tok = token.Token(token.EOF, self.file.char())
		elif self.file.char().isalpha():
			tok = self.instruction_token()
		else:
			tok = token.Token(token.ILLEGAL, self.file.char())
			self.file.read_char()

		return tok

	def skip_whitespace(self):
		while self.file.char().isspace():
			self.file.read_char()

	def instruction_token(self):
		str = self.read()
		instr = token.get_instruction(str)
		return token.Token(instr, str)

	def read(self):
		str = ''

		while not self.file.char().isspace() and self.file.char() != ',':
			str += self.file.char()
			self.file.read_char()
		return str
