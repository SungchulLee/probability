import numpy as np


def main():
    n = 100
    n_simulation = 10000
    x = np.arange(n)

    num_f_with_fixed_points = 0
    for i in range(n_simulation):
        y = np.random.permutation(n)
        if np.sum(x == y) > 0:
            num_f_with_fixed_points += 1

    # prob_A : probability of choosing f with fixed points
    prob_A_by_simulation = num_f_with_fixed_points / n_simulation

    # prob_B : probability of choosing f with no fixed points
    prob_of_no_fied_points_by_simulation = 1 - prob_A_by_simulation
    prob_of_no_fied_points_by_approximation = np.exp(-1)

    print(f"{prob_of_no_fied_points_by_simulation = }")
    print(f"{prob_of_no_fied_points_by_approximation = }")

if __name__ == "__main__":
    main()