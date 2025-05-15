import urllib.request

def getpage(url):
    response = urllib.request.urlopen(url)
    raw = response.read()
    return raw.decode("utf-8")



