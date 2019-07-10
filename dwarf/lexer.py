from . import token

class Lexer(object):
	
	def __init__(self, filename):
		with open(filename) as f:
			self.source = f.read()

		self.char = ''
		self.readPosition = 0
	
	def tokenize(self):
		tokens = []

		while self.char != token.EOF:
			tokens.append(self._nextToken())

		return tokens

	def _nextToken(self):
		self._skipWhitespace()

		if self._isRegister():
			return self._registerToken()
		elif self._isBinaryLiteral():
			return self._binaryLiteralToken()
		elif self._isEOF():
			return token.Token(token.EOF)
		else:
			return self._instructionToken()

	def _skipWhitespace(self):
		while self._isWhitespace():
			self._readChar()

	def _isWhitespace(self):
		return self.char.isspace() or self.char == ','

	def _isBinaryLiteral(self):
		return self.char == '0' and self._peekChar() == 'b'

	def _isRegister(self):
		return self.char == '$'

	def _isEOF(self):
		return self.char == token.EOF

	def _registerToken(self):
		return token.Token(token.REGISTER, self._read())
			
	def _binaryLiteralToken(self):
		return token.Token(token.BINARY_LITERAL, self._read())

	def _instructionToken(self):
		instr = self._read()
		instrToken = token.InstructionType.get(instr)

		if instrToken is None:
			return token.Token(token.ILLEGAL)

		return token.Token(instrToken)

	def _read(self):
		token = ''

		while not self._isWhitespace():
			token += self.char
			self._readChar()

		return token

	def _readChar(self):
		if len(self.source) <= self.readPosition:
			self.char = token.EOF
		else:
			self.char = self.source[self.readPosition]
			self.readPosition += 1

	def _peekChar(self):
		if len(self.source) <= self.readPosition:
			return token.EOF
		else:
			return self.source[self.readPosition]
