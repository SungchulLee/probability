import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.arange(1,N_MAX) 
    pmf = stats.geom(P).pmf(x)
    cdf = stats.geom(P).cdf(x)

    _, ax = plt.subplots(1,1,figsize=(12,4))
    ax.bar(x,cdf,alpha=0.2,color='red',label='CDF')
    ax.bar(x,pmf,label='PMF')
    ax.legend()
    ax.set_title(f'Geometric Goe({P})', fontsize=20)
    plt.show()

if __name__ == "__main__":
    main()