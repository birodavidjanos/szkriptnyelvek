def main():
    numbers=[]
    for i in range(1,101):
        numbers.append(str(i))

    Total_sum=0
    for number in numbers:
        for digit in number:
            Total_sum+=int(digit)

    print('Az elso 100 szam osszege:', Total_sum)
    print("Számok listája:", numbers)

if __name__ == "__main__":
    main()