LUI = 'LUI'
ORI = 'ORI'
LB  = 'LB'
REGISTER = 'REGISTER'
BINARY_LITERAL = 'BINARY_LITERAL'
ILLEGAL = 'ILLEGAL'
EOF = 'EOF'


class Token(object):

	def __init__(self, type, literal=''):
		self.type = type
		self.literal = literal

	def __str__(self):
		return "Token({}, {})".format(self.type, self.literal)


InstructionType = {
	'lui': LUI,
	'ori': ORI,
	'lb': LB,
}
