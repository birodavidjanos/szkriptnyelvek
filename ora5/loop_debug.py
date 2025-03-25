def debug(number, debug=False):
    # If debug mode is enabled, print the start message, the range in one line, and the end message
    if debug:
        print("Start loop")  # Indicate the start of the loop in debug mode
        print(" ".join(str(i) for i in range(1, number+1)))  # Convert the range to a single line string
        print("End loop")  # Indicate the end of the loop in debug mode
    else:
        # If debug mode is disabled, print the range in one line without start/end messages
        print(" ".join(str(i) for i in range(1, number+1)))  # Convert the range to a single line string

def main():
    # Call the debug function with number=5 and debug=True to print debug messages
    debug(5, True)  # Debug mode with detailed output
    # Call the debug function with number=6 and default debug=False for plain output
    debug(6)        # Non-debug mode with simple output

# Entry point of the program
main()
