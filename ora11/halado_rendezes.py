def func1(tp):
    return tp[-1]


def func2(lista):
    return int(lista.split(':')[0])

def func3(matrix):
    return sorted(matrix, key=lambda x: x[1])

def main():
    data = [ 
        (1, 'Albany', 'NY', 162692),
        (121, 'Wyoming', 'NY', 8722),
        (3, 'Allegany', 'NY', 11986),
        (123, 'Yates', 'NY', 5094)
    ]

    result=sorted(data,key=func1)
    result=sorted(data,key=lambda data:data[-1])
    print(result)

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    result=sorted(users,key=func2,reverse=True)
    print(result)

    matrix = [ [2, 6], [1, 3], [5, 4] ]
    

    print(func3(matrix))


if __name__ == "__main__":
    main()