from model import Coin

def main():
    obj = Coin()
    print(obj.run_MC(num_steps=5, seed=1))

if __name__ == "__main__":
    main()