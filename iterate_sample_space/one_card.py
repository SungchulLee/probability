def main():
    suits = 'SHDC'
    ranks = 'A23456789TJQK'
    for a in suits: 
        for b in ranks:
            print(a+b)

if __name__ == "__main__":
    main()