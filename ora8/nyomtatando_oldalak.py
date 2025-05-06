def nyomtat(st):

    oldalak=st.split(",")
    print(oldalak)

    for i in oldalak:
        if '-' in i:

            hossz=i.split('-')
            for j in range(int(hossz[0]),int(hossz[1])+1):
                print(j,end=' ')

        else:
            print(i,end=' ')

def main():
    nyomtat("1-4,7,9,11-15")

if __name__ == "__main__":
    main()
