import numpy as np
from scipy import  special 

from global_name_space import ARGS

def main():
    # computation of beta function using scipy.special 
    print(f"{special .beta(ARGS.alpha, ARGS.beta) = }")

    # computation of beta function using numpy 
    x = np.linspace(0., 1., num=1000, endpoint=False)
    f = x**(ARGS.alpha-1) * (1-x)**(ARGS.beta-1)
    dx = x[1] - x[0]
    integral = np.sum(f*dx)
    print(f"{integral = }")

if __name__ == "__main__":
    main()