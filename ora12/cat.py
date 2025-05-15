import sys
#python cat.py 1.txt 2.txt 3.txt


def cat(fname):
    try:    
        with open(fname) as f:
            print(f"---{fname}---")
            content=f.read()
            print(content)
    except FileNotFoundError:
        print("Hiba a file megnyitasakor")

def main():
    args=sys.argv[1:]
    for arg in args:
        cat(arg)

if __name__=='__main__':
    main()