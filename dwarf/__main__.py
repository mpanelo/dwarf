import argparse
from .file import File
from .lexer import Lexer
from .parser import Parser


def main():
    args = _parse_args()
    file = File(args.filename)
    lexer = Lexer(file)
    parser = Parser(lexer)
    program = parser.parse_program()
    print(program)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()


if __name__ == '__main__':
    main()
