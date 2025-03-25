def main():
    # Convert all items in the list to uppercase and add an exclamation mark
    original1 = ['auto', 'villamos', 'metro']
    result = [item.upper() + '!' for item in original1]
    print(result)

    # Capitalize the first letter of each name in the list
    original2 = ['aladar', 'bela', 'cecil']
    result2 = [item.capitalize() for item in original2]
    print(result2)

    # Create a list of 10 zeros
    result3 = [0 for _ in range(10)]
    print(result3)

    # Multiply each number in the list by 2
    original4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result4 = [item * 2 for item in original4]
    print(result4)

    # Convert all strings in the list to integers
    original5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result5 = [int(item) for item in original5]
    print(result5)

    # Convert each character in the string to an integer
    original6 = "1234567"
    result6 = [int(char) for char in original6]
    print(result6)

    # Find the length of each word in the sentence
    original7 = "The quick brown fox jumps over the lazy dog"
    result7 = [len(szo) for szo in original7.split()]
    print(result7)

    # Get the first letter of each word in the sentence
    original8 = "python is an awesome language"
    result8 = [szo[0] for szo in original8.split()]
    print(result8)

    # Create a list of tuples containing each word and its length
    original9 = "The quick brown fox jumps over the lazy dog"
    result9 = [(szo, len(szo)) for szo in original9.split()]
    print(result9)

    # Create a list of even numbers from 0 to 9
    result10 = [x for x in range(10) if x % 2 == 0]
    print(result10)

    # Create a list of squares of even numbers from 0 to 19
    result11 = [x**2 for x in range(20) if x % 2 == 0]
    print(result11)

    # Create a list of squares of numbers from 0 to 19 where the last digit is 4
    result12 = [x**2 for x in range(20) if (x**2) % 10 == 4]
    print(result12)

    # Generate a string of all uppercase letters (A-Z) using their ASCII codes
    result13 = ''.join([chr(code) for code in range(65, 91)])
    print(result13)

    # Remove leading and trailing whitespace from each string in the list
    original14 = [' apple ', ' banana ', ' kiwi']
    result14 = [item.strip() for item in original14]
    print(result14)

    # Convert a list of 1s and 0s into a single string
    original15 = [1, 0, 1, 1, 0, 1, 0, 0]
    result15 = ''.join([str(item) for item in original15])
    print(result15)

if __name__ == "__main__":
    main()

