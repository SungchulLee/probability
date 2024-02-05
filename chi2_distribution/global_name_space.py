import argparse

parser = argparse.ArgumentParser(description='mnist')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

ARGS.df = 5