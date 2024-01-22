A = {2,4,6}
B = {2,4,5}

def main():
    C = (A | B) # A union B 
    D = A.union(B) 

    print(f"{C = }")
    print(f"{D = }")

if __name__ == "__main__":
    main()