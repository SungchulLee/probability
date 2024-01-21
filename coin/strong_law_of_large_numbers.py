import matplotlib.pyplot as plt
import numpy as np

from model import Coin

def main():
    p = 0.5
    obj = Coin(p=p)

    n = 20
    c = obj.run_MC(num_steps=n, seed=3)
    cum_n = np.arange(1,n+1) # number of coin flips so far
    cum_c_expected = 0.5 * cum_n # expected number of coin flips so far
    cum_c = c.cumsum() # number of heads so far

    fig, ax = plt.subplots(figsize=(12,3))
    ax.plot(cum_n,cum_c/cum_n,"-o",label='realized average')
    ax.plot(cum_n,cum_c_expected/cum_n,'--r',label='expected average')
    ax.legend()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0,1.1)
    plt.show()

if __name__ == "__main__":
    main()