import matplotlib.pyplot as plt
import numpy as np

from global_name_space import *


def simulate_ppp_using_coin(ax):
    x = np.random.binomial(1, P, size=(int(N*T),))
    coin = []
    for i, x_ in enumerate(x):
        if x_:
            coin.append(i/N)
    ax.plot(coin,np.zeros_like(coin),'o',color='red',label="ppp using coin")


def main():
    _, ax = plt.subplots(1,1,figsize=(12,1))
    simulate_ppp_using_coin(ax)
    #simulate_ppp_using_expon(ax)
    ax.legend(loc='upper right')
    ax.axis('off')
    plt.show()


if __name__ == "__main__":
    main()