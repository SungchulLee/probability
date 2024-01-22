import itertools as it
import numpy as np

def main():
    for dice_rolls in it.product(np.arange(1,7), repeat=2):
        print(dice_rolls)

if __name__ == "__main__":
    main()