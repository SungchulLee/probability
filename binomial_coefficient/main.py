import numpy as np
import scipy.special as special

if 0:
    n = 3
    k = 2
elif 0:
    n = [10, 11] 
    k = [ 3,  4] 
elif 1:
    n = np.array([10, 11]) 
    k = np.array([ 3,  4]) 

def main():
    n_choose_k = special.comb(n, k)

    print("n          : ", n)
    print("k          : ", k)
    print("n_choose_k : ", n_choose_k)

if __name__ == "__main__":
    main()