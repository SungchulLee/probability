import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.linspace(0,4,100)
    pdf = stats.expon(scale=BT).pdf(x)
    sample = stats.expon(scale=BT).rvs(N)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x,pdf,label='pdf')
    ax.hist(sample, density=True, bins=np.linspace(0,4,100), color='b', alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()