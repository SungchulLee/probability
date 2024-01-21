import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.arange(0,30)
    pmf = stats.poisson(LA).pmf(x)
    cdf = stats.poisson(LA).cdf(x)
    samples = stats.poisson(LA).rvs(N)

    _, (ax0, ax1, ax2) = plt.subplots(1,3,figsize=(12,4))
    ax0.plot(x,pmf,'--r')
    ax1.plot(x,cdf)
    ax2.hist(samples, bins=x-0.5, density=True, histtype='step', label="hist")
    ax2.plot(x, pmf, '--r', label="pmf")
    ax2.legend()
    ax0.set_title(f'PMF of Po({LA})')
    ax1.set_title(f'CDF of Po({LA})')
    ax2.set_title(f'Hist of Po({LA}) Samples')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()