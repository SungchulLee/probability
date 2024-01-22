import itertools as it
import numpy as np

# sample space of rolling dice n times
def sample_space(n):
    a = it.product(np.arange(1,7), repeat=n)
    return {x for x in a}

# event of total sum equals to k, when we roll dice n times
def event(n,k):
    a = set()
    for x in it.product(np.arange(1,7), repeat=n): 
        if np.sum(x) == k:
            a.add(x)
    return a

# probability of total sum equals to k, when we roll dice n times
def probability(n,k):
    return len(event(n,k)) / len(sample_space(n)) 

# probability estimation using simulation
def probability_simulation(n, k, n_simulation):
    x = np.random.randint(1, 7, (n_simulation, n))
    x_sum = np.sum(x, axis=1) 
    return np.sum(x_sum==k) / n_simulation 

def main():
    # print exact probability
    print("Probability: ", probability(2,5))

    # print probability estimate
    print("Probability estimation using simulation: ", probability_simulation(2,5,1000))

if __name__ == "__main__":
    main()