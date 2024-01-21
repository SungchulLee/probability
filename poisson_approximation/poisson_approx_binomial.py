import matplotlib.pyplot as plt
import numpy as np

from global_name_space import *

def main():
    # generate random samples of binomial distribution B(n,p)
    bin_samples = np.random.binomial(N, P, (N_SAMPLES,))

    # generate random samples of Poisson distribution Po(la)
    po_samples = np.random.poisson(LA, (N_SAMPLES,))

    # plot histogram of generated random samples of binomial distribution B(n,p)
    _, (ax0, ax1, ax2) = plt.subplots(1,3,figsize=(12,3))

    ax0.set_title("Binomial Samples")
    ax0.hist(bin_samples, bins=np.arange(int(3*LA)), density=True)

    ax1.set_title("Poisson Samples")
    ax1.hist(po_samples, bins=np.arange(int(3*LA)), density=True)

    ax2.set_title("Poisson Approximation of Binomial")
    ax2.hist(bin_samples, bins=np.arange(int(3*LA)), density=True,
            label='Binomial Samples', color='b', alpha=1, histtype='step',
            linewidth=4)
    ax2.hist(po_samples, bins=np.arange(int(3*LA)), density=True,
            label='Poisson Samples', color='r', alpha=0.3, histtype='step',
            linewidth=4)
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()