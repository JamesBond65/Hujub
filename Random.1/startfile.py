import os
from os import getcwd

directory = getcwd()
filename = directory + r'\Random.1\dist\update.exe'

print(filename)
os.startfile(filename)