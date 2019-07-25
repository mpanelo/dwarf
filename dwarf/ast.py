class Program(object):
    def __init__(self):
        self.instructions = []

    def __str__(self):
        s = 'Program:\n'
        for instruction in self.instructions:
            s += '\t{}\n'.format(instruction)
        return s

    def append(self, instruction):
        self.instructions.append(instruction)


class RFormatStatement(object):
    def __init__(self, instr_token, reg_token):
        self.instr_token = instr_token
        self.reg_token = reg_token

    def __str__(self):
        return 'RFormatStatement({}, {})'.format(self.instr_token,
                                                 self.reg_token)


class IFormatStatement(object):
    def __init__(self, instr_token, reg_token, binary_token):
        self.instr_token = instr_token
        self.reg_token = reg_token
        self.binary_token = binary_token

    def __str__(self):
        return 'IFormatStatement({}, {}, {})'.format(self.instr_token,
                                                     self.reg_token,
                                                     self.binary_token)


class Instruction(object):
    @classmethod
    def get(cls, instr):
        pass


class Register(object):
    pass


class Binary(object):
    pass
