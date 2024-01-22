import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def main():
    sample_size = 10000
    mu = 0
    sigma = 10
    n = 10

    # sampling from normal distribution
    x = np.random.normal(mu, sigma, (n, sample_size)) 

    x_bar = np.sum(x, axis=0) / n 
    s_square = np.sum((x - x_bar)**2, axis=0) / (n-1)
    s = np.sqrt(s_square)

    # sampling from t distribution with degree n-1
    t = (x_bar - mu) / (s/np.sqrt(n)) 

    _, ax = plt.subplots(figsize=(12,3))
    _, bins, _ = ax.hist(t, bins=np.arange(-6,6,0.1), density=True) 
    y = stats.t(df=n-1).pdf(bins)
    ax.plot(bins,y,"--r",label="pdf",lw=3)
    ax.set_title('$t_{}$'.format(n-1))
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()