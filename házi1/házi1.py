def is_palindrome_simple(s: str) -> bool:
    return s == s[::-1]


def is_palindrome_iterative(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_recursive(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


print(is_palindrome_simple("görög"))  
print(is_palindrome_simple("palindrom")) 
print(is_palindrome_iterative("görög"))  
print(is_palindrome_iterative("palindrom"))  
print(is_palindrome_recursive("görög"))  
print(is_palindrome_recursive("palindrom"))  
