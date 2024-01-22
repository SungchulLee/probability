import argparse
import numpy as np

parser = argparse.ArgumentParser(description='mnist')
parser.add_argument('--seed', type=int, default=0, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--distribution', type=int, default=0, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.n = 2
ARGS.n_sim = 10_000