import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    data = np.random.randn(10_000)

    fig, ax = plt.subplots(figsize=(12,3))
    _, x, _ = ax.hist( data, bins=100, density=True, alpha=0.3 )
    y = stats.norm().pdf(x)
    ax.plot(x,y,'--r',lw=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position('zero')
    plt.show()

if __name__ == "__main__":
    main()