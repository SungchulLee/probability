import itertools as it

def main():
    for i in it.product(['H', 'T'], repeat=3):
        print(i)

if __name__ == "__main__":
    main()