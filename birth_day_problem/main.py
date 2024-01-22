import numpy as np
import matplotlib.pyplot as plt

def main():
    # probability_B[k] - probability that first k  people have all different birthdays
    probability_B = np.zeros(100)
    for k in range(100):
        if (k==0) or (k==1):
            probability_B[k] = 1
        else:
            probability_B[k] = probability_B[k-1] * (1-((k-1)/365)) 

    # probability_A[k] - probability that there is birthday match among first k
    probability_A = np.array(1 - probability_B)
    idx = np.where(probability_A>=0.5)[0][0]
        
    plt.plot(probability_A)
    plt.plot(np.ones_like(probability_A)*0.5,'--b',alpha=0.4)
    plt.plot([idx,idx],[0,probability_A[idx]],"--or")
    plt.title("Bithday Matching Probability")
    plt.xlabel('Number_People')
    plt.ylabel('Probability')
    plt.show()

    print("Smallest number of people with bithday matching prob more than half: ", idx)

if __name__ == "__main__":
    main()