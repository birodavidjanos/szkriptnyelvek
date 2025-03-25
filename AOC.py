AOC.py

def main():
    """
    Processes a text file of numbers, calculates a custom sum, and prints results.

    Steps:
    1. Opens and reads a file line by line.
    2. Prints each line’s content after stripping whitespace.
    3. Applies a rule to sum digits: a digit adds to the sum if it matches the next one (circular comparison).
    4. Outputs the final calculated sum.

    Note: Ensure the file path and content format are correct.
    """

    

    with open(r"C:\Users\student\Downloads\day01.txt", "r") as f:
   
        for line in f:
            number = line.strip()

            print("New line:")
           
   
    
    osszeg=0
    hossz=len(number)
    print("Number:",number,"\nHossz:",hossz,"| Tipus:",type(number))
    hossz=hossz-1

    for i in range(0,hossz+1):
        if i!=hossz:
            if number[i]==number[i+1]:
                osszeg+=int(number[i])
        elif i==hossz:
            if number[i]==number[0]:
                osszeg+=int(number[i])

    print("Eredmény:",osszeg)


if __name__ == "__main__":
    main()
