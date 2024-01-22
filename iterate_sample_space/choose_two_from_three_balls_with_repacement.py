import itertools as it

def main():
    for i in it.combinations_with_replacement(['red','green','blue'], 2):
        print(i)

if __name__ == "__main__":
    main()