import numpy as np
import matplotlib.pyplot as plt

from global_name_space import ARGS

def main():
    x_sample = np.random.choice(ARGS.x, size=ARGS.n_sim, p=ARGS.pmf) 

    plt.hist(x_sample)
    plt.show()

if __name__ == "__main__":
    main()