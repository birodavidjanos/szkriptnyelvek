import json

def main():
    # Open and read the JSON file
    with open('primes.json', 'r') as file:
        data = json.load(file)

    counter=0
    for szam in data:
        if str(szam)==str(szam)[-1]:
            print(szam)
            counter+=1
    
    print(counter)
if __name__ == '__main__':
    main()