import argparse
import numpy as np

parser = argparse.ArgumentParser(description='mnist')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.loc = 0
ARGS.scale = 1
ARGS.n_samples = 10_000