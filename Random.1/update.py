import time
import tkinter as tk
import requests
from tkinter import messagebox, ttk
import webbrowser
from os import getcwd
import urllib.request as ur
from os import remove
from sys import argv
import os
from os import getcwd

directory = getcwd()
filename = directory + r'\Random.1\dist\update.exe'
os.startfile(filename)




def mise_a_jour():

    
    version=1.0
    Nom_application='ScredAIO'
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/JamesBond65/Hujub/master/Random.1/version.txt')
        data = float(response.text)
        

        if float(data) > float(version):
            messagebox.showinfo('Software Update', 'Update Available!')
            message = messagebox.askyesno('Update !', f'{Nom_application} {version} needs to update to version {data}')
            if message is True:
                       
                
                
                directory = getcwd()
                #print(directory)
                filename = directory + '\Version_+_Executable\ScredAIO1.exe'
                #print(filename)
                
                headers = {
                    'Authorization': 'token 8328bc8c4501732d3d47053e00299eb52abfec2f',
                    'Accept': 'application/vnd.github.v3.raw',
                        }

                r = requests.get(
                    'https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Bot_Zalando_3.0/Test_telechargement_du_.exe/update.exe', 
                    headers=headers, allow_redirects=True)
                

                f = open(filename,'wb')
                f.write(r.content)
                version=data

                directory = getcwd()
                filename = directory + r'\Random.1\dist\update.exe'
                os.startfile(filename)
                
                
                #remove(argv[0])

                pass


            else:
                pass
        else:
            #messagebox.showinfo('Software Update', 'No Updates are Available.')
            pass
            
    except Exception as e:
        messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

    
        




mise_a_jour()

nombre = int(input("entrer un nombre et je le multiplie par 2 :"))
nombre=nombre*2
print(nombre)
time.sleep(5)