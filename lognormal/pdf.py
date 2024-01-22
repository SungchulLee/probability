import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    data = stats.lognorm(s=ARGS.s,scale=ARGS.scale).rvs(10_000, random_state=ARGS.seed)

    _, ax = plt.subplots(figsize=(12, 3))

    _, bins, _ = ax.hist(data, bins=np.linspace(0,20,100), density=True, alpha=0.7)
    y = stats.lognorm(s=ARGS.s,scale=ARGS.scale).pdf(bins)
    ax.plot(bins, y, '--r', lw=3)
    ax.set_title("lognorm sampling")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position('zero')

    plt.show()

if __name__ == "__main__":
    main()