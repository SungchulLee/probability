import numpy as np

def main():
    n = 100
    x = np.random.uniform(0, 1, (1, n))
    y = x + np.random.uniform(0, 1, (1, n))
    z = x + y + np.random.uniform(0, 1, (1, n))
    X = np.vstack([x,y,z])

    print(np.cov(X)) # sample covariance
    print(np.var(X)) # population variance
    print(np.corrcoef(X)) # correlation coefficient

if __name__ == "__main__":
    main()