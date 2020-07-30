import requests
from os import getcwd
import urllib.request as ur


url = 'https://raw.github.com/JamesBond65/Hujub/master/Random.1/dist/update.exe'
#r = requests.get(url, allow_redirects=True)

directory = getcwd()
print(directory)
filename = directory + '\Random.1\ScredAIO.exe'
print(filename)
r = requests.get(url, allow_redirects=True)

f = open(filename,'wb')
f.write(r.content)
'''


f = ur.urlopen(url)
file = f.read()
f.close()
f2 = open('download.exe', 'wb')
f2.write(file)
f2.close()'''