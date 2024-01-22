import itertools as it
import numpy as np

def main():
    Omega = set(it.product(np.arange(1,7), repeat=2))
    print(Omega)

if __name__ == "__main__":
    main()