import random

def shuffled(lista):
    lista1=lista.copy()
    random.shuffle(lista1)
    return lista1
def randomc(lista):
    lista1=lista.copy()
    random.shuffle(lista1)
    return lista1[0]

def main():

    lista=[1,2,3,4,5,6]
    print(shuffled(lista))
    print(randomc(lista))

if __name__ == "__main__":
    main()