import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    samples_bernoulli = np.random.binomial(1, ARGS.p, size=(ARGS.n, ARGS.n_sim))
    samples_binomial = samples_bernoulli.sum(axis=0)

    x = np.arange(ARGS.n+1) 
    pmf = stats.binom(ARGS.n,ARGS.p).pmf(x)

    _, ax = plt.subplots(1,1,figsize=(12,4))
    ax.set_title(f'Binomial B({ARGS.n},{ARGS.p})', fontsize=20)

    ax.bar(x,pmf,alpha=0.3,label='PMF')

    bins = np.array([-1,0,1,2,3,4]) - 0.5
    plt.hist(samples_binomial, density=True, bins=bins, histtype='step', label="sum of bernoulli")

    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()