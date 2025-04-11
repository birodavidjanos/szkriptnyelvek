def is_balanced(expr):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack  # ha üres a stack, minden rendben


def main():
    print(is_balanced("((5+3)*2+1)"))
    print(is_balanced("{[(3+1)+2]+}")) 
    print(is_balanced("(3+{1-1)}"))
    print(is_balanced("[1+1]+(2*2)-){3/3}"))
    print(is_balanced("(({[(((1)-2)+3)-3]/3}-3)"))

if __name__=="__main__":
    main()