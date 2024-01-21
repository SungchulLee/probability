import matplotlib.pyplot as plt
import numpy as np

from global_name_space import *

def main():
    N_SAMPLES = 10_000 # number of samples to generate

    # generate random samples of \sum_{i=1}^n X_i where X_i \sim B(p_i)
    n = 1000
    P = np.random.uniform(0.,1., (n,1)) / 100 # p is not fixed, but small random
    uniform_samples = np.random.uniform(0., 1., (n, N_SAMPLES))
    X_i = (uniform_samples > 1-P)
    S_n = np.sum(X_i, axis=0)

    # generate random samples of Poisson distribution Po(la)
    LA = np.sum(P)
    po_samples = np.random.poisson(lam=LA, size=N_SAMPLES)

    # plot histogram of generated random samples of binomial distribution B(n,p)
    _, (ax0, ax1, ax2) = plt.subplots(1,3,figsize=(12,3))

    ax0.set_title("Indicators Sum Samples")
    ax0.hist(S_n, bins=np.arange(int(3*LA)), density=True)

    ax1.set_title("Poisson Samples")
    ax1.hist(po_samples, bins=np.arange(int(3*LA)), density=True)

    ax2.set_title("Poisson Approximation of Indicators Sum")
    ax2.hist(S_n, bins=np.arange(int(3*LA)), density=True,
            label='Indicators Sum Samples', color='b', alpha=1, histtype='step',
            linewidth=4)
    ax2.hist(po_samples, bins=np.arange(int(3*LA)), density=True,
            label='Poisson Samples', color='r', alpha=0.3, histtype='step',
            linewidth=4)
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()