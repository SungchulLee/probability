import numpy as np

def main():
    n = 100
    x = np.random.uniform(0, 1, (1, n))

    print("sample variance")
    print(np.cov(x)) # sample variance
    print(np.sum((x-(np.sum(x)/n))**2)/(n-1)) # sample variance

    print("population variance")
    print(np.var(x)) # population variance
    print(np.sum((x-(np.sum(x)/n))**2)/n) # population variance

if __name__ == "__main__":
    main()