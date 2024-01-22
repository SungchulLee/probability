import itertools as it

def main():
    for coin_flip, dice_roll in it.product(['H', 'T'], [1, 2, 3, 4, 5, 6]):
        print(coin_flip, dice_roll)

if __name__ == "__main__":
    main()