import matplotlib.pyplot as plt
import scipy.stats as stats

from global_name_space import ARGS

def main():
    data = stats.f(ARGS.df1,ARGS.df2).rvs(10_000, random_state=ARGS.seed)

    _, ax = plt.subplots(figsize=(12,3))
    _, x, _ = ax.hist(data, bins=100, density=True, alpha=0.7)
    y = stats.f(ARGS.df1,ARGS.df2).pdf(x)
    ax.plot(x,y,'--r',lw=3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position('zero')
    plt.show()

if __name__ == "__main__":
    main()