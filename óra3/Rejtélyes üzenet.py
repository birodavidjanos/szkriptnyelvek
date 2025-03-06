def rejtelyesuzenet(szoveg):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Abc = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"

    result = ""



    for i in UZENET:
        if i in abc:
            result += Abc[abc.find(i)]
        else:
            result += i

    return result

UZENET = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def main():
    print(rejtelyesuzenet(UZENET))

if __name__ == "__main__":
    main()    