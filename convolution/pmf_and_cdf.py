import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    x = np.arange(ARGS.n+1) 
    pmf = stats.binom(ARGS.n,ARGS.p).pmf(x)
    cdf = stats.binom(ARGS.n,ARGS.p).cdf(x)

    _, ax = plt.subplots(1,1,figsize=(12,4))
    ax.bar(x,cdf,alpha=0.2,color='red',label='CDF')
    ax.bar(x,pmf,label='PMF')
    ax.legend()
    ax.set_title(f'Binomial B({ARGS.n},{ARGS.p})', fontsize=20)
    plt.show()

if __name__ == "__main__":
    main()