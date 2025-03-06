#!/usr/bin/env python3

import sys


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    #if inp == 'y' or inp == 'Y' or inp == 'yes':    # <- egyszerűbben?
    if inp.lower().startswith("y"):    
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')

##############################################################################

if __name__ == "__main__":
    main()