import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    if ARGS.distribution == 0: # exponential 
        samples = np.random.exponential(scale=1/0.5, size=(ARGS.n_max,ARGS.n_sim)).cumsum(axis=0) # scale=1/lambda
    elif ARGS.distribution == 1: # poisson
        samples = np.random.poisson(lam=0.5, size=(ARGS.n_max,ARGS.n_sim)).cumsum(axis=0) 
    elif ARGS.distribution == 2: # uniform
        samples = np.random.uniform(-0.5, 0.5, (ARGS.n_max,ARGS.n_sim)).cumsum(axis=0)

    _, axes = plt.subplots(1,ARGS.n_max,figsize=(20,3))
    for i, (ax, sample) in enumerate(zip(axes,samples),start=1):
        ax.hist(sample,bins=100,density=True)
        ax.set_title(f"dist of S_{i}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()