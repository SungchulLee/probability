import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    n = 10_000                           # Number of random samples generated
    x = np.random.uniform(0, 1, (n,2)) # 0th column = height of lower end, 1st column = angle/pi 
    h = x[:,0] + np.sin(np.pi*x[:,1])  # Height of higher end
    N = np.sum(h>=1)                   # Number of random samples hit the upper bar at y=1
    Estimated_pi = 2*n/N               # Estimated pi

    print("Number of Needles             : ", n)
    print("Monte Carlo Estimate of $\pi$ : ", Estimated_pi)

    # plot of Monte Carlo Estimate of $\pi$ 
    # as a function of Number of Buffon's Needles 
    N_cum = np.cumsum(h>=1) 
    Estimated_pi_cum = 2*(np.arange(0,n)+1)/(N_cum+0.00000001) 
    plt.plot(Estimated_pi_cum[6:])
    plt.plot(np.ones_like(Estimated_pi_cum[6:])*np.pi,"--r")
    plt.show()

if __name__ == "__main__":
    main()