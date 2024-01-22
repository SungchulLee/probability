import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    N_POINTS = 100

    # Random points in unit square 
    x = np.random.uniform(0, 1, (2, N_POINTS))
    r_square = np.sum(x**2, axis=0)

    # Random points in unit square - red if points are inside unit circle, unit circle added
    plt.axis([0,1,0,1]) # [xmin, xmax, ymin, ymax]
    boundary_x = np.linspace(0, 1, 100)
    boundary_y = np.sqrt(1 - boundary_x**2)
    plt.plot(boundary_x, boundary_y, 'r')
    for i in range(N_POINTS):
        if x[0,i]**2 + x[1,i]**2 <1:
            plt.plot(x[0,i], x[1,i], 'ro')
        else:
            plt.plot(x[0, i], x[1, i], 'bo')
    plt.axis("equal")
    plt.show()

    print("Number of generated points: ", N_POINTS)
    print("Estimation of pi:           ", (4/N_POINTS) * np.sum(r_square < 1))

if __name__ == "__main__":
    main()