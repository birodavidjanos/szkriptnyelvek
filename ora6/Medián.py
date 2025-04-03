def test(lista):
    lista.sort()  # Fontos: rendezzük a listát
    hossz = len(lista)

    if hossz % 2 == 0:
        index = hossz // 2
        return (lista[index - 1] + lista[index]) / 2  # Két középső elem átlaga
    else:
        index = hossz // 2
        return lista[index]  # Középső elem

def main():
    print(test([1, 2, 3, 4, 5]) == 3)
    print(test([3, 1, 2, 5, 3]) == 3)
    print(test([1, 300, 2, 200, 1]) == 2)
    print(test([3, 6, 20, 99, 10, 15]) == 12.5)

if __name__ == '__main__':
    main()
