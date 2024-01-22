import matplotlib.pyplot as plt
import numpy as np

def main():
    # number of random samples of number of couples with same birthday
    n_samples = 100_000

    # generate random samples of number of couples with same birthday
    n = 80_000
    p = 1/365
    la = n*p
    samples_binomial = np.random.binomial(n, p, (n_samples,))
    samples_poisson = np.random.poisson(la, (n_samples,))

    _, (ax0, ax1) = plt.subplots(1,2,figsize=(12,3))

    ax0.hist(samples_binomial, np.arange(150,300), density=True)
    ax0.set_title("n_couples_with_same_birthday samples using binomial")

    ax1.hist(samples_poisson, np.arange(150,300), density=True)
    ax1.set_title("n_couples_with_same_birthday samples using poisson")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


