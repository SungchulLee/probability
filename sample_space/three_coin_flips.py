import itertools as it

def main():
    Omega = set(it.product(['H', 'T'], repeat=3))
    print(Omega)

if __name__ == "__main__":
    main()