import numpy as np

from global_name_space import ARGS

class Coin:
    def __init__(self, p=0.5):
        """
        p         : probability of head
        """
        self.p = p

    def run_MC(self, num_paths=1, num_steps=100, seed=None):
        """
        num_paths : number of paths to generate
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        if seed is not None:
            np.random.seed(seed)

        return np.random.binomial( n=1, p=self.p, size=( num_paths, num_steps ) )