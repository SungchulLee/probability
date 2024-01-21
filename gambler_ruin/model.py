import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS


class Coin:
    def __init__(self, p=0.5):
        """
        p         : probability of head
        """
        self.p = p

    def run_MC(self, num_paths=1, num_steps=100, seed=None):
        """
        num_paths : number of paths to generate
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        if seed is not None:
            np.random.seed(seed)

        return np.random.binomial( n=1, p=self.p, size=( num_paths, num_steps ) )


class GamblerRuin(Coin):
    def __init__(self, p=0.49, initial=100, goal=200):
        """
        p         : probability of head
        """
        self.p = p
        self.q = 1 - self.p
        self.initial = initial
        self.goal = goal
        self.bankrupt = 0

    def run_MC(self, num_paths=1, num_steps=100, seed=None, verbose=False):
        """
        num_paths : number of paths to generate
        num_steps : number of coin flips to make a sample path
        seed      : seed of random number generator
        """
        coin = 2 * super().run_MC(num_paths, num_steps, seed) - 1
        path = self.initial + np.concatenate([np.zeros((num_paths,1)),coin.cumsum(axis=1)],axis=1)
        gambler_ruin_result = np.zeros((num_paths,))
        for i in range(num_paths):
            for position in path[i]:
                if position == self.goal:
                    gambler_ruin_result[i] = 1
                    break
                if position == self.bankrupt:
                    gambler_ruin_result[i] = -1
                    break

        num_win = gambler_ruin_result[gambler_ruin_result==1].sum()
        num_loss = - gambler_ruin_result[gambler_ruin_result==-1].sum()
        prob_loss_simulation = num_loss / ( num_win + num_loss )
        if verbose:
            print(f"{num_paths = }")
            print(f"{num_win = }")
            print(f"{num_loss = }")
            print(f"ruin probability by simulation : {prob_loss_simulation:.2%}")
        return path, gambler_ruin_result, num_paths, num_win, num_loss, prob_loss_simulation

    def compute_ruin_probability(self, verbose=False):
        # IQ = AQ + b
        I = np.eye(self.goal+1)
        A = self.p*np.eye(self.goal+1, k=1) + self.q*np.eye(self.goal+1, k=-1)
        A[0,1] = 0
        A[-1,-2] = 0
        b = np.zeros((self.goal+1,1))
        b[0,0] = 1

        Q = np.linalg.solve(I-A,b).reshape(self.goal+1)
        if verbose:
            print(f"Minimum initial capital with ruin probability less than half where {self.p = } : ", np.where(Q<=0.5)[0][0])
        return Q


def main():
    p = 0.49
    initial = 10
    goal = 20
    gambler = GamblerRuin(p=p, initial=initial, goal=goal)

    num_paths = 1
    num_steps = 40
    path, gambler_ruin_result, *_ = gambler.run_MC(num_paths=num_paths, num_steps=num_steps,seed=0)
    print(f"{gambler_ruin_result = }")

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(path[0],'-b')
    ax.plot(np.zeros_like(path[0]),'--r')
    ax.plot(np.ones_like(path[0])*goal,'--r')
    plt.show()

if __name__ == "__main__":
    main()