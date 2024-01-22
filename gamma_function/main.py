import numpy as np
from scipy import  special 

from global_name_space import ARGS

def main():
    # computation of gamma function using scipy.special 
    print(f"{special.gamma(ARGS.alpha) = }")

    # computation of gamma function using numpy 
    x = np.linspace(0., 100, num=1000, endpoint=False)
    f = x**(10-1) * np.exp(-x)
    dx = x[1] - x[0]
    integral = np.sum(f*dx)
    print(f"{integral = }")

if __name__ == "__main__":
    main()