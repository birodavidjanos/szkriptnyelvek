#!/usr/bin/env python3
import sys

"""
This script prints the English alphabet in lowercase in either normal 
order or reverse order, depending on how it is executed.

If run as `a-z.py`, it prints the alphabet from 'a' to 'z'.
If run as `z-a.py` (via a symbolic link to `a-z.py`), it prints the 
alphabet in reverse order from 'z' to 'a'.

Commands to set up and run:
    1. Make `a-z.py` executable:
       chmod +x a-z.py
    2. Create a symbolic link named `z-a.py`:
       ln -sf a-z.py z-a.py
    3. Run the scripts:
       ./a-z.py    # Prints: abcdefghijklmnopqrstuvwxyz
       ./z-a.py    # Prints: zyxwvutsrqponmlkjihgfedcba
"""

def main():
    """
    Determines the execution context and prints the English alphabet 
    in normal or reverse order based on the script name.

    If the script name ends with `z-a.py`, the alphabet is printed 
    in reverse order. Otherwise, it is printed in normal order.
    """
    if sys.argv[0].endswith("z-a.py"):
        print("".join(reversed("abcdefghijklmnopqrstuvwxyz")))
    else:
        print("abcdefghijklmnopqrstuvwxyz")

if __name__ == "__main__":
    main()
