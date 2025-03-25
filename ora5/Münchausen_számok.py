def Munchausen(num):
    """
This program identifies Münchausen numbers within a specified range.

A Münchausen number is a natural number where the sum of each digit raised
to the power of itself equals the original number. By convention, 0**0 is
considered 0. For example:
    - 1 is a Münchausen number because 1**1 = 1.
    - 3435 is a Münchausen number because 3**3 + 4**4 + 3**3 + 5**5 = 3435.

Functions:
    - Munchausen(num): Determines whether a given number is a Münchausen number.
        Args:
            num (int): The number to be checked.
        Returns:
            bool: True if the number is a Münchausen number, False otherwise.
        Method:
            Precomputes a dictionary of powers for digits 0-9 to optimize
            calculations. Then sums the appropriate power for each digit in
            the input number.

    - main(): Iterates through numbers from 0 to 440 million and prints all
              Münchausen numbers found in that range.

Usage:
    Run the script as a standalone program. The results are printed directly
    to the console.

Example Output:
    1
    3435
    438579088
"""

    powers = {str(d): d**d if d != 0 else 0 for d in range(10)}
    sum = 0
    for char in str(num):
        sum += powers[char]
    return sum == num

def main():
    for i in range(0, 440000000):  
        if Munchausen(i):
            print(i)

if __name__ == "__main__":
    main()
