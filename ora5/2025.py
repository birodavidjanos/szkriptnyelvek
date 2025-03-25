def main():
    """
    Prints the concatenated lengths of strings in a predefined list.

    The function iterates over a list of strings, calculates the length of
    each string using the len() function, and prints the lengths without
    spaces or separators in between. The output is a single concatenated
    string of the lengths.

    Example:
        Given the list ["az", "", "az", "vlmia"], the function prints "2025",
        as the lengths of the strings are 2, 0, 2, and 5 respectively.
    """
    szoveg=["az","","az","vlmia"]
    for i in szoveg:
        print(len(i),end='')

if __name__ == "__main__":
    main()
