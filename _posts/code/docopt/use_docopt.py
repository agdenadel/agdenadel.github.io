"""Usage: use_docopt.py [-s=<win>] <input> <output>

Process input and write text file output. Uses window size provided, or default of 10.

Arguments:
  input          required input file
  output         required output file

Options:
  -h --help.      Show this screen.
  -s=<win> --size       Window Size [default: 10].
"""
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    # do stuff


if __name__ == '__main__':
    main()