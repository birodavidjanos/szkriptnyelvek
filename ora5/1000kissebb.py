def main():
    """
    Calculates and prints the sum of all numbers below 1000 
    that are divisible by either 3 or 5.

    This function uses a generator expression to iterate through 
    numbers from 0 to 999. It checks if each number is divisible 
    by 3 or 5, sums up the qualifying numbers, and prints the result.

    Example:
        The result printed by the function:
        >>> 233168
    """
    print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))


if __name__ == "__main__":
    main()
