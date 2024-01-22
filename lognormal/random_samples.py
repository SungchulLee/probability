import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    data = stats.lognorm(s=ARGS.s,scale=ARGS.scale).rvs(10_000, random_state=ARGS.seed)
    data_from_norm = np.exp(stats.norm(loc=ARGS.mu,scale=ARGS.sigma).rvs(size=10_000, random_state=ARGS.seed))

    _, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))

    _, bins, _ = ax0.hist(data, bins=np.linspace(0,20,100), density=True, alpha=0.7)
    y = stats.lognorm(s=ARGS.s,scale=ARGS.scale).pdf(bins)
    ax0.plot(bins, y, '--r', lw=3)
    ax0.set_title("lognorm sampling")

    ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7)
    ax1.plot(bins, y, '--r', lw=3)
    ax1.set_title("lognorm sampling using normal")

    for ax in (ax0, ax1):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_position('zero')

    plt.show()

if __name__ == "__main__":
    main()


