import argparse
from dwarf.lex.ioreader import IOReader
from dwarf.lex.lexer import Lexer
from dwarf.parse.parser import Parser
from dwarf import emulator


def main():
    args = parse_args()
    if args.repl:
        emulate_stdin()
    else:
        emulate_file(args.filename)


def emulate_file(filename):
    ioreader = IOReader.from_file(filename)
    lexer = Lexer(ioreader)
    parser = Parser(lexer)
    emulator.emulate(parser.parse_program())


def emulate_stdin():
    while True:
        data = input(">> ")
        ioreader = IOReader(data)
        lexer = Lexer(ioreader)
        parser = Parser(lexer)
        print(parser.parse_program())


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', dest='filename')
    group.add_argument('--repl', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    main()
