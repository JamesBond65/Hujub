import tkinter as tk
import requests
from tkinter import messagebox, ttk
import webbrowser
from os import getcwd
import urllib.request as ur
from os import remove
from sys import argv
import os
import time

def mise_a_jour():

    directory = os.path.dirname(os.path.realpath(__file__))
    nom_rename = directory + '\Rename.exe'

    def checkFileExistance(filePath):
        try:
            with open(filePath, 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False

    if checkFileExistance(nom_rename) == True :
        os.remove(nom_rename)

    version=0.9
    Nom_application='ScredAIO'

    try:
        #token = 'token a2fce3ce396b83dec87df039eb7531f201bac641'
        headers = {
                    'Authorization': token,
                    'Accept': 'application/vnd.github.v3.raw',
                        }

        response = requests.get(
            'https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Version_%2B_Executable/Version.txt', 
            headers=headers, allow_redirects=True)
        
        data = float(response.text)
        
        if float(data) > float(version):
            messagebox.showinfo('Software Update', 'Update Available!')
            message = messagebox.askyesno('Update !', f'{Nom_application} {version} needs to update to version {data}')
            if message is True:
                       
                directory = os.path.dirname(os.path.realpath(__file__))
                
                filename = directory + '\ScredAIO-1.exe'
                #print(filename)
                
                headers = {
                    'Authorization': token,
                    'Accept': 'application/vnd.github.v3.raw',
                        }

                r = requests.get(
                    'https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Version_%2B_Executable/ScredAIO-1.exe', 
                    headers=headers, allow_redirects=True)
                
                f = open(filename,'wb')
                f.write(r.content)
                f.close()

                r = requests.get(
                    'https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Version_%2B_Executable/Rename.exe', 
                    headers=headers, allow_redirects=True
                )

                f= open(nom_rename, 'wb')
                f.write(r.content)
                f.close()
                version=data

                os.startfile(nom_rename)
                
                pass

            else:
                pass
        else:
            messagebox.showinfo('Software Update', 'No Updates are Available.')
            
    except Exception as e:
        messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))
