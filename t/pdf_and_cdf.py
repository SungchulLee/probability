import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    x = np.linspace(-3,3,100)
    pdf = stats.t(df=ARGS.df).pdf(x)
    cdf = stats.t(df=ARGS.df).cdf(x)

    _, ax = plt.subplots()
    ax.plot(x,pdf,label='pdf')
    ax.plot(x,cdf,label='cdf')
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title(f"pdf and cdf of t_{ARGS.df}")
    plt.show()

if __name__ == "__main__":
    main()