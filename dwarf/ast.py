from . import token


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


class Instruction(object):
    def __init__(self, instr_token):
        self.instr_token = instr_token

    @property
    def id(self):
        if hasattr(self, 'INSTR_ID'):
            return self.INSTR_ID[self.instr_token.literal]
        raise RuntimeError("INSTR_ID attribute is not set!")


class RTypeInstruction(Instruction):
    LB = 0
    PUSH = 1

    INSTR_ID = {
        token.LB: LB,
        token.PUSH: PUSH,
    }

    def __init__(self, instr_token, reg_token):
        super().__init__(instr_token)
        self.register = Register(reg_token)

    def __str__(self):
        return "{:<5} {:<7}".format(self.instr_token.literal, self.register)


class ITypeInstruction(Instruction):
    ORI = 2
    LUI = 3

    INSTR_ID = {
        token.LUI: LUI,
        token.ORI: ORI,
    }

    def __init__(self, instr_token, bin_token):
        super().__init__(instr_token)
        self.binary = Binary(bin_token)

    def __str__(self):
        return "{:<5} {:<7}, {:<7}".format(self.instr_token.literal,
                                           self.register, self.binary)


class Register(object):
    R0 = 0
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7

    REG_ID = {
        token.REG0: R0,
        token.REG1: R1,
        token.REG2: R2,
        token.REG3: R3,
        token.REG4: R4,
        token.REG5: R5,
        token.REG6: R6,
        token.REG7: R7,
    }

    def __init__(self, reg_token):
        self.reg_token = reg_token

    @property
    def id(self):
        return self.REG_ID[self.reg_token.literal]

    def __str__(self):
        return "{}".format(self.reg_token.literal)

    def __format__(self, format_spec):
        return str(self)


class Binary(object):
    def __init__(self, bin_token):
        self.bin_token = bin_token

    @property
    def as_int(self):
        return int(self.bin_token.literal, 2)

    def __str__(self):
        return "{}".format(self.bin_token.literal)

    def __format__(self, format_spec):
        return str(self)
