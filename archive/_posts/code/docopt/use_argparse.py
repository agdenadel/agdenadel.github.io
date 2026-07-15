import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("input", help="The input text file", type=str)
    parser.add_argument("output", help="The input text file", type=str)
    parser.add_argument("-s", "--size", help="Integer window size", default=10, type=int)

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # do stuff


if __name__ == '__main__':
    main()