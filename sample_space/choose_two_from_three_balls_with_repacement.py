import itertools as it

def main():
    Omega =  set(it.combinations_with_replacement(['red','green','blue'], 2))
    print(Omega)

if __name__ == "__main__":
    main()