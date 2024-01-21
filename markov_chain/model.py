import matplotlib.pyplot as plt
import numpy as np

from global_name_space import *


class MarkovChain:
    def __init__(self, transition_probs, initial_distribution, np_seed=1):
        self.P = transition_probs
        self.pi = initial_distribution
        np.random.seed(np_seed)

        self.num_states = len(initial_distribution)
        self.states = np.arange(self.num_states)
        self.current_state = None

    def reset(self):
        self.current_state = np.random.choice(self.states, p=self.pi)

    def step(self):
        self.current_state = np.random.choice(self.states,
                                              p=self.P[self.current_state, :])


class TransProb:
    def __init__(self, trans_prob_name='random', np_seed=1):
        self.np_seed = np_seed

        if trans_prob_name == 'random':
            np.random.seed(self.np_seed)
            N_STATES = 4
            self.transition_probs = np.random.normal(0., 1., (N_STATES, N_STATES))
            self.transition_probs = np.exp(self.transition_probs)
            self.transition_probs = self.transition_probs / np.sum(self.transition_probs, axis=1).reshape((N_STATES, 1))

        elif trans_prob_name == 'homogeneous':
            np.random.seed(self.np_seed)
            N_STATES = 4
            self.transition_probs = np.empty((N_STATES, N_STATES))
            l = 0.4
            r = 0.4
            s = 1 - l - r
            #                                  0  1  2      3
            self.transition_probs[0, :] = [s + l, r, 0,     0]
            self.transition_probs[1, :] = [    l, s, r,     0]
            self.transition_probs[2, :] = [    0, l, s,     r]
            self.transition_probs[3, :] = [    0, 0, l, s + r]

        elif trans_prob_name == 'non-homogeneous':
            np.random.seed(self.np_seed)
            N_STATES = 4
            self.transition_probs = np.empty((N_STATES, N_STATES))
            #                                 0   1    2    3
            self.transition_probs[0, :] = [0.1, 0.9,   0,   0]
            self.transition_probs[1, :] = [0.1, 0.6, 0.3,   0]
            self.transition_probs[2, :] = [  0, 0.5, 0.4, 0.1]
            self.transition_probs[3, :] = [  0,   0, 0.7, 0.3]

        self.num_states = self.transition_probs.shape[0]
        self.initial_distribution = np.ones((self.num_states,)) / self.num_states


def run(mc, n_steps=100):
    state_history = []

    mc.reset()
    state_history.append(mc.current_state)
    for _ in range(n_steps):
        mc.step()
        state_history.append(mc.current_state)
    return state_history


def draw(state_history):
    _, ax = plt.subplots(figsize=(12,4))
    ax.plot(state_history)
    ax.set_yticks([0, 1, 2, 3])
    plt.show()



def main():
    if 0:
        env = TransProb(trans_prob_name='random')
    elif 0:
        env = TransProb(trans_prob_name='homogeneous')
    elif 1:
        env = TransProb(trans_prob_name='non-homogeneous')

    P = env.transition_probs
    initial_distribution = env.initial_distribution

    mc = MarkovChain(P, initial_distribution)
    state_history = run(mc, n_steps=N_STEPS)
    draw(state_history)


if __name__ == "__main__":
    main()