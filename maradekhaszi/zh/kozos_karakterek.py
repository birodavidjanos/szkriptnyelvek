import sys

def main():
    n=len(sys.argv)
    lista=[]
    betulista=[]

    for i in range(1,n):
        lista.append(sys.argv[i])   

    for szo in lista:
        for betu in szo:
            for szo1 in lista:
                if betu in szo1:
                    if betu not in betulista:
                        betulista.append(betu)
                else:
                     break
            
    for betu in betulista:    
        print(betu,end=' ')

if __name__ == '__main__':
    main()