import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

from global_name_space import ARGS

def main():
    x = np.linspace(0,5,100)
    pdf = stats.f(ARGS.df1,ARGS.df2).pdf(x)
    cdf = stats.f(ARGS.df1,ARGS.df2).cdf(x)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x,pdf,'-',label=f'pdf')
    ax.plot(x,cdf,'-',label=f'cdf')
    ax.set_title(f'f({ARGS.df1},{ARGS.df2})')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()