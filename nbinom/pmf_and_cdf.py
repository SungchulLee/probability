import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import *

def main():
    x = np.arange(R,N_MAX+1) 
    # Note my definition of negative binomial is different from stats.nbinom.
    # stats.geom counts head and I also count head. 
    # stats.nbinom does not count head, whereas I count head. 
    # Here, I use my definition of the negative binomial, 
    # which is coherent with the definition of the geometric distribution. 
    # With my definition, I can say that 
    # if $X_i$ are iid with Geo(p), 
    # then $X_1+\cdots+X_r$ is $NB(r,p)$.
    pmf = stats.nbinom(R,P).pmf(x-R)
    cdf = stats.nbinom(R,P).cdf(x-R)

    _, ax = plt.subplots(1,1,figsize=(12,4))
    ax.bar(x,cdf,alpha=0.2,color='red',label='CDF')
    ax.bar(x,pmf,label='PMF')
    ax.legend()
    ax.set_title(f'Negative Binomial NB({R},{P})', fontsize=20)
    plt.show()

if __name__ == "__main__":
    main()