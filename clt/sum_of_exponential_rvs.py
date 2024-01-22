import matplotlib.pyplot as plt
import numpy as np

def main():
    # Sum of Exponential Random Variables
    n_sum = 4
    num_samples = 1000
    x = np.random.exponential(size=(num_samples, n_sum))
    x = np.sum(x,axis=1)

    # plot pdf of samples using plt.hist 
    plt.hist(x, bins=25, color='red', alpha=0.5, density=True) 

    # estimate mu and sigma from the sample
    mu_hat = np.sum(x) / num_samples
    sigma_square_hat = np.sum((x - mu_hat)**2) / num_samples
    sigma_hat = np.sqrt(sigma_square_hat)

    # compute pdf of normal distribution with estimated mu and sigma
    xp = mu_hat + sigma_hat * np.linspace(-3,3,100) # x values where we compute pdf
    yp = np.exp(-(xp-mu_hat)**2/(2*sigma_hat**2)) / np.sqrt(2*np.pi*sigma_hat**2) # computed pdf values

    # plot pdf of normal distribution with estimated mu and sigma 
    plt.plot(xp,yp,'--r')
    plt.show()

if __name__ == "__main__":
    main()