import argparse
from .lexer import Lexer


def main():
	args = _parse_args()
	lexer = Lexer(args.filename)
	for token in lexer.tokenize():
		print(token)


def _parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	return parser.parse_args()


if __name__ == '__main__':
	main()
