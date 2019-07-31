class Memory(object):
    def __init__(self, size):
        self.memory = bytearray(size)

    def __setitem__(self, location, value):
        self.memory[location] = value

    def __getitem__(self, location):
        return self.memory[location]

    def __str__(self):
        return '[' + ','.join([str(el) for el in self.memory]) + ']'


class RegisterFile(Memory):
    pass


class RegisterStack(object):
    def __init__(self):
        self.stack = []

    def push(self, register):
        self.stack.append(register)

    def pop(self):
        if not self.stack:
            raise HardwareError("Stack has no items to pop!")
        return self.stack.pop()


class HardwareError(Exception):
    pass
