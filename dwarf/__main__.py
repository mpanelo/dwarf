import argparse
from .lexer import Lexer
from .parser import Parser


def main():
    args = parse_args()
    if args.repl:
        emulate_stdin()
    else:
        emulate_file(args.filename)


def emulate_file(filename):
    with open(filename) as f:
        data = f.read()

    lexer = Lexer(data)
    parser = Parser(lexer)
    print(parser.parse_program())


def emulate_stdin():
    while True:
        data = input(">> ")

        lexer = Lexer(data)
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
