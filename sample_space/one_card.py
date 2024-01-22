def main():
    Omega = set()
    suits = 'SHDC'
    ranks = 'A23456789TJQK'
    for a in suits: 
        for b in ranks:
            Omega.add(a+b)
    print(Omega)

if __name__ == "__main__":
    main()