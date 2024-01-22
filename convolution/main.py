import numpy as np
import matplotlib.pyplot as plt

from global_name_space import ARGS
from load_data import load_data

def main():
    data = load_data()
    samples = np.sum(data, axis=0)

    plt.hist(samples, density=True, bins=100)
    plt.show()

if __name__ == "__main__":
    main()