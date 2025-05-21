def main():
    with open('corpus.txt', encoding='utf-8') as f:
        lines = [line.strip().split(",")[0] for line in f]  # Szavak beolvasása
    
    print('Talált szavak:')
    for word in lines:
        index_j = word.lower().find("j")
        index_s = word.lower().find("s", index_j + 1)
        index_u = word.lower().find("u", index_s + 1)
        index_n = word.lower().find("n", index_u + 1)

        if index_j != -1 and index_s != -1 and index_u != -1 and index_n != -1:
            print(word)

if __name__ == '__main__':
    main()
