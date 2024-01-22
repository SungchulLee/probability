import numpy as np
import matplotlib.pyplot as plt

from global_name_space import ARGS

def sample_x(probability_mass_function):
    pmf = probability_mass_function
    cdf = np.cumsum(pmf)
    uni = np.random.rand(1)
    cdf_minus_uni = cdf - uni
    return [ n for n,i in enumerate(cdf_minus_uni) if i>0 ][0]

def main():
    x_sample = []
    for _ in range(ARGS.n_sim): 
        temp = sample_x(probability_mass_function=ARGS.pmf)
        x_temp = ARGS.x[temp]
        x_sample.append(x_temp)

    plt.hist(x_sample)
    plt.show()

if __name__ == "__main__":
    main()