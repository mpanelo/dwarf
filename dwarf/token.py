INSTRUCTION = 'INSTRUCTION'
REGISTER = 'REGISTER'
BINARY = 'BINARY'
ILLEGAL = 'ILLEGAL'
COMMA = 'COMMA'
EOF = 'EOF'

LUI = 'lui'
ORI = 'ori'
LB = 'lb'
SB = 'sb'
PUSH = 'push'
ADD = 'add'

REG0 = '$r0'
REG1 = '$r1'
REG2 = '$r2'
REG3 = '$r3'
REG4 = '$r4'
REG5 = '$r5'
REG6 = '$r6'
REG7 = '$r7'


class Token(object):
    def __init__(self, type, literal=''):
        self.type = type
        self.literal = literal

    def __str__(self):
        return "Token({}, {})".format(self.type, self.literal)
