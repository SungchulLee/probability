import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    mu = 0
    sigma = 1

    x = mu + 3*sigma*np.linspace(-1,1,100)
    pdf = stats.norm(mu,sigma).pdf(x)
    cdf = stats.norm(mu,sigma).cdf(x)

    _, ax = plt.subplots()
    ax.plot(x,pdf,label='pdf')
    ax.plot(x,cdf,label='cdf')
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend()
    ax.set_title("pdf and cdf of standard normal")
    plt.show()

if __name__ == "__main__":
    main()