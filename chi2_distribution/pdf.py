import matplotlib.pyplot as plt
import scipy.stats as stats

from global_name_space import ARGS

def main():
    data = stats.chi2(df=ARGS.df).rvs(10_000, random_state=ARGS.seed)

    _, ax = plt.subplots(figsize=(12, 3))

    _, bins, _ = ax.hist(data, bins=100, density=True, alpha=0.7)
    y = stats.chi2(df=ARGS.df).pdf(bins)
    ax.plot(bins, y, '--r', lw=3)
    ax.set_title("chi square sampling")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position('zero')

    plt.show()

if __name__ == "__main__":
    main()