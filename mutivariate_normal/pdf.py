import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    # Number of points in each direction
    n = 40

    # Parameters
    mu_1 = 0
    mu_2 = 0
    sigma_1 = 1
    sigma_2 = 0.5
    rhos = (0.0, -0.8, 0.8)

    # Create a grid and a multivariate normal
    x = np.linspace(-3.0, 3.0, n)
    y = np.linspace(-3.0, 3.0, n)
    X, Y = np.meshgrid(x, y)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y
    Z = lambda rho: stats.multivariate_normal([mu_1, mu_2], [[sigma_1, rho*sigma_1*sigma_2],
                                                            [rho*sigma_1*sigma_2, sigma_2]])

    fig, axes = plt.subplots(1, 3, figsize=(15,5), subplot_kw={'projection': '3d'})

    for ax, rho in zip(axes, rhos):
        ax.plot_surface(X, Y, Z(rho).pdf(pos), cmap='viridis', linewidth=0)
        ax.set_title(f"{rho = }")
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.view_init(80, -90)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()