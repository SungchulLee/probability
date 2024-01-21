import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg

from global_name_space import *
from model import MarkovChain, TransProb


def compute_stationary_distribution(P, n_states):
    A = np.c_[P - np.eye(n_states), np.ones((n_states,1))]
    b = np.zeros((1, n_states+1)); b[0,-1] = 1
    pi, *_ = linalg.lstsq(A.T, b.T)
    pi = pi.T
    return pi


def run(mc, n_states, n_steps):
    visit_log = np.zeros((n_states,n_steps))
    mc.reset()
    visit_log[mc.current_state, 0] = 1.
    for step in range(1, n_steps):
        mc.step()
        visit_log[mc.current_state, step] = 1.

    pi_ = np.cumsum(visit_log, axis=1) / (np.arange(n_steps) + 1).reshape((1,-1))
    return pi_


def draw(pi, pi_, n_states, n_steps):
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12, 6), sharex=True)
    for s in range(n_states):
        axes[s].plot(pi_[s], label="empirical stationary distribution prob")
        axes[s].plot([0, n_steps-1], [pi[0,s], pi[0,s]], '--', label="stationary distribution prob")
        axes[s].legend(loc='upper right')
        axes[s].set_ylim([0., 1.])
        axes[s].legend(loc=2)
        axes[s].set_title(f"state {s}")
    plt.tight_layout()
    plt.show()


def main():
    if 1:
        env = TransProb(trans_prob_name='random')
    elif 0:
        env = TransProb(trans_prob_name='homogeneous')
    elif 1:
        env = TransProb(trans_prob_name='non-homogeneous')

    P = env.transition_probs
    n_states = env.num_states
    initial_distribution = env.initial_distribution

    # stationary distribution
    pi = compute_stationary_distribution(P, n_states)

    mc = MarkovChain(P, initial_distribution, np_seed=1)

    # empirical stationary distribution
    pi_ = run(mc, n_states, N_STEPS)

    draw(pi, pi_, n_states, N_STEPS)


if __name__ == "__main__":
    main()