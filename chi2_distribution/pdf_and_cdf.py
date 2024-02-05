import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    x = np.linspace(0,30,100)
    pdf = stats.chi2(df=ARGS.df).pdf(x)
    cdf = stats.chi2(df=ARGS.df).cdf(x)

    _, ax = plt.subplots(figsize=(12, 3))

    ax.plot(x,pdf,label="pdf")
    ax.plot(x,cdf,label="cdf")

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title(f"pdf and cdf of t_{ARGS.df}")
    plt.show()

if __name__ == "__main__":
    main()