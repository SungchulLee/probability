import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from model import Coin

def main():
    p = 0.5
    q = 1 - p
    obj = Coin(p=p)

    num_paths = 10_000
    num_steps = 10_000
    seed = 0
    c = obj.run_MC(num_paths=num_paths, num_steps=num_steps, seed=seed)
    cumsum = c.cumsum(axis=1) # number of heads so far

    _, (ax0,ax1,ax2,ax3) = plt.subplots(1,4,figsize=(15,4))
    bins = np.linspace(-4,4,61)
    y = stats.norm().pdf(bins)
    ax0.hist((cumsum[:,10-1]-p*10)/np.sqrt(10*p*q),density=True,alpha=0.5,bins=bins)
    ax1.hist((cumsum[:,100-1]-p*100)/np.sqrt(100*p*q),density=True,alpha=0.5,bins=bins)
    ax2.hist((cumsum[:,1_000-1]-p*1_000)/np.sqrt(1_000*p*q),density=True,alpha=0.5,bins=bins)
    ax3.hist((cumsum[:,10_000-1]-p*10_000)/np.sqrt(10_000*p*q),density=True,alpha=0.5,bins=bins)
    for ax, n_flips in zip((ax0,ax1,ax2,ax3),(10,100,1_000,10_000)):
        ax.set_title("(observed - expected) / sd \nwith n_flips = {:,}".format(n_flips))
        ax.set_xlim(-4,4)
        ax.set_ylim(0,2)
        ax.plot(bins,y,'--r')
    plt.show()

if __name__ == "__main__":
    main()