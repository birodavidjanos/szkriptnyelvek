#!/usr/bin/env python3

import json

def main():
    f=open("person.json")

    d=json.load(f)
    print(d)
    print(d["daughter"]["age"])

    f.close()

if __name__=="__main__":
    main()