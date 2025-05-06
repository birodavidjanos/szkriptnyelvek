def prim_palindrom(szam: int) -> bool:
   
    if str(szam) != str(szam)[::-1]:  
        return False
    
    if szam < 2:
        return False  

    for i in range(2, int(szam**0.5) + 1):  
        if szam % i == 0:
            return False
    return True

def legkisebb_prim_palindrom(N: int) -> int:
   
    while True:
        if prim_palindrom(N):
            return N
        N += 1

def main() -> None:

    print(legkisebb_prim_palindrom(131)) 
    print(legkisebb_prim_palindrom(130)) 
    print(legkisebb_prim_palindrom(31))  
    print(legkisebb_prim_palindrom(1977))

if __name__ == "__main__":
    main()
