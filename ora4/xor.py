def xorr(str1,str2):
    if (bool(str1)==True and bool(str2)==False) or (bool(str1)==False and bool(str2)==True):
        print("True") 
    else:
        print("False")

def main():
    xorr("szia",None)

if __name__ == "__main__":
    main()