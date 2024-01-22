import numpy as np
import scipy.stats as stats

def main():
    x = np.random.uniform(0, 1, (1000,))

    # kurtosis is normalized so that it is zero for the normal distribution
    # Excess_Kurtosis(X) = Kurtosis(X) − 3
    print("Minimum:            ", np.min(x))
    print("Maximum:            ", np.max(x))
    print("Mean:               ", np.mean(x))
    print("Median:             ", np.median(x))
    print("Variance:           ", np.var(x)) # population variance
    print("Standard deviation: ", np.std(x))
    print("Skewness:           ", stats.skew(x))
    print("Kurtosis:           ", stats.kurtosis(x)) # Excess_Kurtosis(X)

if __name__ == "__main__":
    main()