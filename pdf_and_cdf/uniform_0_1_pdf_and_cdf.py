import matplotlib.pyplot as plt
import numpy as np

pdf = lambda x: 1 * (0 <= x) * (x <= 1)
cdf1 = lambda x: 0 * (x < 0)
cdf2 = lambda x: x * (0 <= x) * (x <= 1)
cdf3 = lambda x: 1 * (1 < x)
cdf = lambda x: cdf1(x) + cdf2(x) + cdf3(x)

def main():
    x = np.linspace(-1, 2, 100)
    pdf_values = pdf(x)
    cdf_values = cdf(x)

    _, axes = plt.subplots(1,2,figsize=(12,3))
    for ax, values, title in zip(axes, (pdf_values, cdf_values), ("pdf", "cdf")):
        ax.plot(x, values)
        ax.set_title(title)
    plt.show()

if __name__ == "__main__":
    main()