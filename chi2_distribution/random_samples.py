import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    data = stats.chi2(df=ARGS.df).rvs(10_000, random_state=ARGS.seed)
    data_from_norm = np.sum(stats.norm().rvs(size=(ARGS.df, 10_000), random_state=ARGS.seed)**2,axis=0)

    _, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))

    _, bins, _ = ax0.hist(data, bins=100, density=True, alpha=0.7)
    y = stats.chi2(df=ARGS.df).pdf(bins)
    ax0.plot(bins, y, '--r', lw=3)
    ax0.set_title("chi square sampling")

    ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7)
    ax1.plot(bins, y, '--r', lw=3)
    ax1.set_title("chi square sampling using normal")

    for ax in (ax0, ax1):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_position('zero')

    plt.show()

if __name__ == "__main__":
    main()


