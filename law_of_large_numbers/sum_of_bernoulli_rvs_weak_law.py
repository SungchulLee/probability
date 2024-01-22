import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    # B(n,p)
    n = 1
    p = 0.5

    n_samples = 10000
    n_coin_flips_for_each_sample = 10000

    a = np.random.binomial(n, p, (n_samples, n_coin_flips_for_each_sample))
    samples = np.sum(a,1) / n_coin_flips_for_each_sample

    _, (ax0, ax1) = plt.subplots(1,2,figsize=(12,3))
    ax0.hist(samples, bins=100, density=True)
    ax0.set_title("central limit theorem")

    ax1.hist(samples, bins=np.linspace(0,1,100), density=True)
    ax1.set_title("weak law of large numbers")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()