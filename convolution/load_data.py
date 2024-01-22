import numpy as np

from global_name_space import ARGS

def load_data():
    if ARGS.distribution == 0:
        data = np.random.uniform(low=-0.5, high=0.5, size=(ARGS.n, ARGS.n_sim)) # (2,4)
    elif ARGS.distribution == 1:
        data = np.random.poisson(size=(ARGS.n, ARGS.n_sim)) # (2,4)
    elif ARGS.distribution == 2:
        data = np.random.exponential(size=(ARGS.n, ARGS.n_sim)) # (2,4)
    elif ARGS.distribution == 3:
        data = np.random.chisquare(3, size=(ARGS.n, ARGS.n_sim)) # (2,4)
    elif ARGS.distribution == 4:
        data = np.random.beta(1, 3, size=(ARGS.n, ARGS.n_sim)) # (2,4)
    elif ARGS.distribution == 5:
        data = np.random.f(3, 3, size=(ARGS.n, ARGS.n_sim)) # (2,4)
    return data