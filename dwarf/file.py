class File(object):

	EOF = 'EOF'

	def __init__(self, filename):
		self.file = open(filename, 'r')
		self.read_char()

	def is_closed(self):
		return self.file.closed

	def char(self):
		return self.ch

	def read_char(self):
		if self.file.closed:
			return self.EOF

		char = self.file.read(1)

		if not char:
			self.file.close()
			self.ch = self.EOF
		else:
			self.ch = char

	def peek_char(self):
		if self.file.closed:
			return self.EOF

		pos = self.file.tell()
		ch = self.file.read(1)
		self.file.seek(pos)

		return ch if ch else self.EOF
