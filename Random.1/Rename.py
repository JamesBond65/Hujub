import os
import time
from sys import argv

time.sleep(1)
directory = os.path.dirname(os.path.realpath(__file__))
old_file_name = directory + '\ScredAIO-1.exe'
new_file_name = directory +'\ScredAIO.exe'
os.remove(new_file_name)

os.rename( old_file_name , new_file_name)
time.sleep(1)
os.startfile(new_file_name)

