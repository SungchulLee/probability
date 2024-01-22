import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    x = np.linspace(0,20,100)
    pdf = stats.lognorm(s=ARGS.s,scale=ARGS.scale).pdf(x)
    cdf = stats.lognorm(s=ARGS.s,scale=ARGS.scale).cdf(x)

    _, ax = plt.subplots(figsize=(12, 3))

    ax.plot(x,pdf,label="pdf")
    ax.plot(x,cdf,label="cdf")

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title(f"pdf and cdf of lognorm with s={ARGS.s}, scale={ARGS.scale:.2f}")
    plt.show()

if __name__ == "__main__":
    main()