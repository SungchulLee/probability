import numpy as np
import matplotlib.pyplot as plt

def main():
    # goal
    N = 100

    # probabilities
    p = 0.49
    q = 1-p

    # IQ = AQ + b
    I = np.eye(N+1)
    A = p*np.eye(N+1, k=1) + q*np.eye(N+1, k=-1)
    A[0,1] = 0
    A[-1,-2] = 0
    b = np.zeros((N+1,1))
    b[0,0] = 1

    Q = np.linalg.solve(I-A,b).reshape(N+1)
    #print(Q.shape)

    plt.plot(Q)
    plt.title("Probability of Ruin")
    plt.xlabel('Initial_Capital')
    plt.ylabel('Probability_Ruin')
    plt.show()

    print("Minimum initial capital with ruin probability less than half: ", np.where(Q<=0.5)[0][0])

if __name__ == "__main__":
    main()