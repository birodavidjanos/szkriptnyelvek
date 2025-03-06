
def product(numbers):
    sum1=1
    for n in numbers:
        sum1=n*sum1
    return sum1

def main():
    numbers=[1,2,2,2]
    print(product(numbers))

if __name__=="__main__":
    main()