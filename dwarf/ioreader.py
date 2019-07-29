class IOReader(object):
    EOF = 'EOF'

    def __init__(self, data):
        self.data = data.strip()
        self.pos = 0

    def end_of_file(self):
        return self.char() == self.EOF

    def char(self):
        try:
            return self.data[self.pos]
        except IndexError:
            return self.EOF

    def read_char(self):
        if not self.end_of_file():
            self.pos += 1

    def peek_char(self):
        self.pos += 1
        ch = self.char()
        self.pos -= 1

        return ch
