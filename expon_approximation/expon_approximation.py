import matplotlib.pyplot as plt
import scipy.stats as stats

from global_name_space import *

def main():
    x_geo = stats.geom(P).rvs(N_SIM) / N

    _, ax = plt.subplots(figsize=(12,3))
    _, bins, _ = ax.hist(x_geo, bins=100, density=True, alpha=0.2, label="geometric/n")
    exp_pdf = stats.expon(scale=BT).pdf(bins)
    ax.plot(bins, exp_pdf, "--r", label="exponential", alpha=0.7)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()