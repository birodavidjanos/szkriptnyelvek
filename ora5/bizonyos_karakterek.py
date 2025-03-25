def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    Returns a string containing only the characters from 'text' that exist in 'chars'.

    Args:
        text (str): The input string to filter.
        chars (str): The set of allowed characters. Defaults to uppercase letters and digits.

    Returns:
        str: A string containing the filtered characters.
    """
    result = ""
    for i in range(len(text)):
        for j in range(len(chars)):
            if text[i] == chars[j]:
                result += text[i]
    return result

def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()