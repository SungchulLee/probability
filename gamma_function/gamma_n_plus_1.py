from scipy import  special 

from global_name_space import ARGS

def main():
    # computation of gamma(n+1) using scipy.special 
    print(f"{special.gamma(ARGS.n+1) = }")

    # computation of n! using scipy.special  
    print(f"{special.factorial(ARGS.n) = }")

if __name__ == "__main__":
    main()