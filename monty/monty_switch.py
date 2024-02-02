import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS
from model import MontySwitch

def main():
    n_tries = 1000
    results = []
    for _ in range(n_tries):
        results.append(MontySwitch().run())

    results = np.array(results)
    cum_success_rates = results.cumsum() / np.arange(1, n_tries+1) 
    plt.plot(cum_success_rates)
    plt.plot(np.ones_like(cum_success_rates)*2/3, "--r")
    plt.show()

if __name__ == "__main__":
    main()