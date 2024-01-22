import argparse
import numpy as np

parser = argparse.ArgumentParser(description='mnist')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.x = [ -3,  -1,   1,   2,   5]
ARGS.pmf = [0.1, 0.1, 0.1, 0.5, 0.2]
ARGS.n_sim = 1000