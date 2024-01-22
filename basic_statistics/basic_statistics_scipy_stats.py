import numpy as np
import scipy.stats as stats

def main():
    x = np.random.uniform(0, 1, (1000,))

    # kurtosis is normalized so that it is zero for the normal distribution
    # Excess_Kurtosis(X) = Kurtosis(X) − 3 
    n, min_max, mean, var, skew, kurt = stats.describe(x)
    print("Number of samples:  ", n)
    print("Minimum of samples: ", min_max[0])
    print("Maximum of samples: ", min_max[1])
    print("Mean:               ", mean)
    print("Variance:           ", var) # population variance
    print("Skewness:           ", skew)
    print("Kurtosis:           ", kurt) # Excess_Kurtosis(X)

if __name__ == "__main__":
    main()