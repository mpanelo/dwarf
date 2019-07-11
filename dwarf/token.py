LUI = 'LUI'
ORI = 'ORI'
LB  = 'LB'
REGISTER = 'REGISTER'
BINARY = 'BINARY'
ILLEGAL = 'ILLEGAL'
COMMA = 'COMMA'
EOF = 'EOF'

instructions = {
	'lui': LUI,
	'ori': ORI,
	'lb': LB,
}

class Token(object):

	def __init__(self, type, literal=''):
		self.type = type
		self.literal = literal

	def __str__(self):
		return "Token({}, {})".format(self.type, self.literal)


def get_instruction(instr):
	return instructions.get(instr, ILLEGAL)
