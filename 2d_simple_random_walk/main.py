import matplotlib.pyplot as plt
import numpy as np
import random; random.seed(337)

def main():
    N_STEPS = 100 # number of steps in simulation

    # define NEWS steps
    N = [ 0,  1]
    E = [ 1,  0]
    W = [-1,  0]
    S = [ 0, -1]

    # 2D simple random walk
    x = [0]
    y = [0]
    for step in range(N_STEPS):
        dx, dy = random.choice([N, E, W, S])
        x.append(x[-1]+dx)
        y.append(y[-1]+dy)

    # plot of 2D simple random walk
    plt.plot(x, y, '-')
    plt.axis([-1.5*np.sqrt(N_STEPS), 1.5*np.sqrt(N_STEPS), -1.5*np.sqrt(N_STEPS), 1.5*np.sqrt(N_STEPS)])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()