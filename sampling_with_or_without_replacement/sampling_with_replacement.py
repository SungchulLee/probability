import numpy as np
import matplotlib.pyplot as plt

def main():
    Omega  = [ -3,  -1,   1,   2,   5]
    pmf    = [0.1, 0.1, 0.1, 0.5, 0.2]
    sample = np.random.choice(Omega, p=pmf, size=(1000,)) 

    plt.hist(sample, bins=np.arange(-3,6))
    plt.show()

if __name__ == "__main__":
    main()