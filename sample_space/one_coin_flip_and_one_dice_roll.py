import itertools as it

def main():
    Omega = set(it.product(['H', 'T'], [1, 2, 3, 4, 5, 6]))
    print(Omega)

if __name__ == "__main__":
    main()