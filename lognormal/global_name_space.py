import argparse
import numpy as np

parser = argparse.ArgumentParser(description='mnist')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

# parameters for X \sim N(mu,sigma**2)
ARGS.mu = 2
ARGS.sigma = 2

# parameters for e^X
ARGS.s = ARGS.sigma
ARGS.scale = np.exp(ARGS.mu)