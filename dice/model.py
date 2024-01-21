import numpy as np

from global_name_space import ARGS


class Dice:
    def run_MC(self, num_paths=1, num_steps=100, seed=None):
        """
        num_paths : number of paths to generate
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        if seed is not None:
            np.random.seed(seed)

        return np.random.randint( low=1, high=7, size=( num_paths, num_steps ) )


def main():
    dice = Dice()
    print(dice.run_MC())

if __name__ == "__main__":
    main()