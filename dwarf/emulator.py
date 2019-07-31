from .hardware import RegisterFile, RegisterStack, Memory

REG_FILE = RegisterFile(size=8)
MEMORY = Memory(size=256)
REG_STACK = RegisterStack()
FLAG = 0  # can be used as ALU's carry or zero flag


def emulate(program):
    emulator = Emulator()

    for instr in program:
        instr.accept(emulator)

    print(MEMORY)
    print(REG_FILE)


class Emulator(object):
    def visit(self, instr):
        method_name = 'visit_{}'.format(instr.name)
        visitor = getattr(self, method_name, self.panic)
        return visitor(instr)

    def panic(self, instr):
        msg = "visit_{} does not exist".format(instr.name)
        raise EmulatorError(msg)

    def visit_add(self, instr):
        x = REG_FILE[REG_STACK.pop()]
        y = REG_FILE[REG_STACK.pop()]

        sum = x + y

        # FLAG = (sum & 0x100) >> 8
        REG_FILE[instr.register_dest] = sum & 0xFF

    def visit_lb(self, instr):
        x = REG_FILE[REG_STACK.pop()]
        REG_FILE[instr.register_dest] = MEMORY[x]

    def visit_sb(self, instr):
        x = REG_FILE[REG_STACK.pop()]
        MEMORY[x] = REG_FILE[instr.register_dest]

    def visit_push(self, instr):
        REG_STACK.push(instr.register_dest)

    def visit_lui(self, instr):
        register = REG_STACK.pop()

        x = REG_FILE[register]

        REG_FILE[register] = ((x << 4) | instr.immediate) << 8

    def visit_ori(self, instr):
        register = REG_STACK.pop()

        x = REG_FILE[register]

        REG_FILE[register] = x | instr.immediate


class EmulatorError(Exception):
    pass
