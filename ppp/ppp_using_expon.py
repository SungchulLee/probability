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


def simulate_ppp_using_expon(ax):
    x = np.random.exponential(scale=BT, size=(int(LA*T)*100,)).cumsum()
    x = x[x<T]
    ax.plot(x,np.ones_like(x),'o',color='blue',label="ppp using expon")


def main():
    _, ax = plt.subplots(1,1,figsize=(12,1))
    simulate_ppp_using_coin(ax)
    simulate_ppp_using_expon(ax)
    ax.legend(loc='center right')
    ax.axis('off')
    plt.show()


if __name__ == "__main__":
    main()