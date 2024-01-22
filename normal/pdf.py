import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    _, (ax0, ax1, ax2) = plt.subplots(1,3,figsize=(12,3))

    # ax0
    mu = 0 # mean 0
    sigma = 1 # standard deviation 1
    x = mu + sigma * np.linspace(-3,3,100)
    y = stats.norm(mu,sigma).pdf(x)
    ax0.plot(x,y,label='mean {}, std {}'.format(mu,sigma))

    # ax1
    mu = 0 # mean 0
    sigmas = np.arange(1,5) # several different standard deviations
    x = np.linspace(-12,12,100)
    for sigma in sigmas:
        y = stats.norm(mu,sigma).pdf(x)
        ax1.plot(x, y, label='std {}'.format(sigma))

    # ax2
    mus = np.arange(-2,3) # several different means
    sigma = 1 # standard deviation 1
    x = np.linspace(-6,6,100)
    for mu in mus:
        y = stats.norm(mu,sigma).pdf(x)
        ax2.plot(x, y, label='mean {}'.format(mu))

    titles = ("standard normal","normal with mean 0","normal with std 1")
    for ax, title in zip((ax0, ax1, ax2), titles):
        ax.set_title(title)
        ax.legend()
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()