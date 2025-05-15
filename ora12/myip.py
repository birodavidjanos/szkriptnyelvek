import urllib.request
import json


def getpage(url):
    response = urllib.request.urlopen(url)
    raw = response.read()
    return raw.decode("utf-8")



def main():

    url = "https://jsonip.com/"
    s=getpage(url)

    p = json.loads(s)
    print("Az én ip cimen:",p['ip'])
    
    
if __name__ == "__main__":
    main()
