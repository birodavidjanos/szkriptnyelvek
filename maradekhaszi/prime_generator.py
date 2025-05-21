import json

def main():
    primek = []

    for i in range(2, 10000):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primek.append(i)
        
    print(primek)
    
     # Kiírás JSON fájlba
    with open("primes.json", "w") as file:
        json.dump(primek, file)

    print(f"{len(primek)} prím kiírva a primes.json fájlba.")

if __name__ == '__main__':
    main()