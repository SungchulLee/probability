import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.linspace(0,4,100)
    pdf = stats.expon(scale=BT).pdf(x)
    cdf = stats.expon(scale=BT).cdf(x)
    sample = stats.expon(scale=BT).rvs(N)

    _, ax = plt.subplots()
    ax.plot(x,pdf,label='pdf')
    ax.plot(x,cdf,label='cdf')
    ax.hist(sample, density=True, bins=x, color='b')
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title("pdf and cdf of standard normal")
    plt.show()

if __name__ == "__main__":
    main()