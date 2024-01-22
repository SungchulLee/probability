import argparse
import numpy as np

parser = argparse.ArgumentParser(description='beta_function')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--distribution', type=int, default=1, metavar='S',
                    help='distribution of X_i')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.n_sim = 10000
ARGS.n_max = 10

if ARGS.distribution == 0: # exponential 
    ARGS.sample = np.random.exponential(scale=1/0.5, size=(ARGS.n_max,ARGS.n_sim)).cumsum(axis=0)