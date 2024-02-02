import matplotlib.pyplot as plt

from model import SimpleRandomWalk

def main():
    model = SimpleRandomWalk()
    t, SRW = model.run_MC()

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(t,SRW[0])
    plt.show()

if __name__ == "__main__":
    main()