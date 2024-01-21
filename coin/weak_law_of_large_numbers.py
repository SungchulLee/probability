import matplotlib.pyplot as plt

from model import Coin


def main():
    p = 0.5
    obj = Coin(p=p)

    num_paths = 10_000
    num_steps = 10_000
    seed = 0
    c = obj.run_MC(num_paths=num_paths, num_steps=num_steps, seed=seed)
    cumsum = c.cumsum(axis=1) # number of heads so far

    fig, (ax0,ax1,ax2,ax3) = plt.subplots(1,4,figsize=(15,4))
    ax0.hist(cumsum[:,10-1]/10,density=True,alpha=0.5,bins=20)
    ax1.hist(cumsum[:,100-1]/100,density=True,alpha=0.5,bins=20)
    ax2.hist(cumsum[:,1_000-1]/1_000,density=True,alpha=0.5,bins=20)
    ax3.hist(cumsum[:,10_000-1]/10_000,density=True,alpha=0.5,bins=20)
    for ax, n_flips in zip((ax0,ax1,ax2,ax3),(10,100,1_000,10_000)):
        ax.set_title("n_heads / n_flips\nwith n_flips = {:,}".format(n_flips))
        ax.set_xlim(0,1)
    plt.show()

if __name__ == "__main__":
    main()