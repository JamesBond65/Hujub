import requests
from os import getcwd
import urllib.request as ur



directory = getcwd()
print(directory)
filename = directory + '\Random.1\ScredAIO.exe'
print(filename)

headers = {
    'Authorization': 'token 166c3f0372a93dd3c1f9e6358e5b39bfb8b57d76',
    'Accept': 'application/vnd.github.v3.raw',
}

r = requests.get('https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Bot_Zalando_3.0/Test_telechargement_du_.exe/update.exe', headers=headers, allow_redirects=True)

f = open(filename,'wb')
f.write(r.content)

TOKEN = "166c3f0372a93dd3c1f9e6358e5b39bfb8b57d76"

