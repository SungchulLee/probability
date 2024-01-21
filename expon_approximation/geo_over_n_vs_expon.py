import matplotlib.pyplot as plt
import scipy.stats as stats

from global_name_space import *

def main():
    x_geo = stats.geom(P).rvs(N_SIM) / N
    x_exp = stats.expon(scale=BT).rvs(N_SIM)

    _, ax = plt.subplots(figsize=(12,3))
    ax.hist(x_geo, bins=100, density=True, alpha=0.2, color='blue', label="Geo/n")
    ax.hist(x_exp, bins=100, density=True, color='red', label="Exp", histtype='step')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()