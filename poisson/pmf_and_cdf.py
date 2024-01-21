import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.arange(0,30)
    pmf = stats.poisson(LA).pmf(x)
    cdf = stats.poisson(LA).cdf(x)

    _, (ax0, ax1) = plt.subplots(1,2,figsize=(12,4))
    ax0.plot(x,pmf,'--r')
    ax1.plot(x,cdf)
    ax0.set_title(f'PMF of Po({LA})')
    ax1.set_title(f'CDF of Po({LA})')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()