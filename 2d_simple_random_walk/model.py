import numpy as np

class SimpleRandomWalk:

    def run_MC(self, num_paths=1, num_steps=100, seed=None):
        """
        num_paths : number of paths to generate
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        if seed is not None:
            np.random.seed(seed)

        Z = np.random.binomial( n = 1, p = 0.5, size = ( num_paths, num_steps ) ) * 2 - 1

        SRW = np.zeros( ( num_paths, num_steps + 1 ) )
        t = np.arange( num_steps + 1 )
        for i in range( 1, num_steps + 1 ):
            SRW[:,i] = SRW[:,i-1] + Z[:,i-1]
        return t, SRW