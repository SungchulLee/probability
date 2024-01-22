import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def main():
    _, ax = plt.subplots(figsize=(12,3))

    x = np.linspace(-3,3)
    for df in [1,3,5,8,50,100]:
        a = stats.t(df)
        y = a.pdf(x)
        ax.plot(x,y,label=f't_{df}')

    a = stats.norm()
    y = a.pdf(x)
    ax.plot(x,y,'-*',label='PDF of Standard Normal')

    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()