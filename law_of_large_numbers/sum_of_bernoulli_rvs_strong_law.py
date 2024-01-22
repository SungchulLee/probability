import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    # B(n,p)
    n = 1
    p = 0.5

    n_simulations = 2_000

    a = np.random.binomial(n, p, (n_simulations,))
    cum_average = np.cumsum(a)/(np.arange(n_simulations)+1)

    plt.plot(cum_average)
    plt.plot(np.ones_like(cum_average)*p,'--r')
    plt.show()

if __name__ == "__main__":
    main()