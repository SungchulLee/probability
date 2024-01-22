import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(9)  

    # sample size
    num_samples = 1000

    # generate normal samples
    x = np.random.normal(2, 2, (num_samples,))

    # plot pdf of samples using plt.hist 
    plt.hist(x, bins=25, color='red', alpha=0.5, density=True) 

    # estimate mu and sigma from the sample
    mu_hat = np.sum(x) / num_samples
    sigma_square_hat = np.sum((x - mu_hat)**2) / (num_samples - 1)
    sigma_hat = np.sqrt(sigma_square_hat)

    ### plot pdf of normal distribution with estimated mu and sigma

    # x values where we compute pdf
    xp = mu_hat + sigma_hat * np.linspace(-3,3,100) 

    # compute pdf values
    yp = np.exp(-(xp-mu_hat)**2/(2*sigma_hat**2)) / np.sqrt(2*np.pi*sigma_hat**2) 

    # plot pdf of normal distribution with estimated mu and sigma 
    plt.plot(xp,yp,'--r')
    plt.show()

if __name__ == "__main__":
    main()