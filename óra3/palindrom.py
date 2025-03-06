def palindrome1_triv(text)->str:
    if text.lower()==text[::-1].lower():
        return True
    else:
        return False

def palindrome1_iter(text):
    hosz=len(text)-1
    i=0
    while i!=hosz:
        if text[i].lower()!=text[hosz-i].lower():
            return False
        i=i+1
    return True


def main():
    print(palindrome1_triv("szia"))
    print(palindrome1_triv("görög"))
    print(palindrome1_triv("mia"))
    print(palindrome1_triv("Anna"))
    print("-.................-")
    print(palindrome1_iter("szia"))
    print(palindrome1_iter("görög"))
    print(palindrome1_iter("mia"))
    print(palindrome1_iter("Anna"))
if __name__ == '__main__':
    main()