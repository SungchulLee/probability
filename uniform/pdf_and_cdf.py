import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    x = np.linspace(ARGS.loc,ARGS.loc+ARGS.scale,100)
    pdf = stats.uniform(loc=ARGS.loc,scale=ARGS.scale).pdf(x)
    cdf = stats.uniform(loc=ARGS.loc,scale=ARGS.scale).cdf(x)
    #sample = stats.uniform(loc=ARGS.loc,scale=ARGS.scale).rvs(ARGS.n_samples)

    _, ax = plt.subplots()
    ax.plot(x,pdf,label='pdf')
    ax.plot(x,cdf,label='cdf')
    #ax.hist(sample, density=True, bins=x, color='b')
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title("pdf and cdf of standard normal")
    plt.show()

if __name__ == "__main__":
    main()