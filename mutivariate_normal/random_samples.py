import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    # Number of points in each direction
    n_sim = 100

    # Parameters
    mu_1 = 0
    mu_2 = 0
    sigma_1 = 1
    sigma_2 = 1
    rho = 0.8

    samples = stats.multivariate_normal([mu_1, mu_2], 
                                       [[sigma_1, rho*sigma_1*sigma_2],
                                        [rho*sigma_1*sigma_2, sigma_2]]).rvs(n_sim)
    # print(samples.shape) # (100, 2)

    _, ax = plt.subplots(figsize=(4,4))

    ax.plot(samples[:,0],samples[:,1],'o')
    ax.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()