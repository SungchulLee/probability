import numpy as np
from scipy import  special 

from global_name_space import ARGS

def main():
    # computation of gamma(n+1) using scipy.special 
    print(f"{special.gamma(1/2) = }")

    # computation of n! using scipy.special 
    print(f"{np.sqrt(np.pi) = }")

if __name__ == "__main__":
    main()