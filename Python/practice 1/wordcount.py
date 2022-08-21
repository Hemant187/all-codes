import urllib.request
url ="https://www.w3.org/TR/PNG/iso_8859-1.txt"
data=urllib.request.urlopen(url).read()
print(data.split())
# print(len(data.split())) 