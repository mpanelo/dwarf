import argparse
from .lexer import Lexer, File


def main():
    args = _parse_args()
    file = File(args.filename)
    lexer = Lexer(file)

    for token in lexer.tokenize():
        print(token)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()


if __name__ == '__main__':
    main()
