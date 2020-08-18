import requests

headers = {
    'Authorization': 'token a2fce3ce396b83dec87df039eb7531f201bac641',
    'Accept': 'application/vnd.github.v3.raw',
                        }
response = requests.get(
    'https://raw.githubusercontent.com/AlexisBal/Projet_Bot/master/Version_%2B_Executable/Version.txt', 
    headers=headers, allow_redirects=True)
        
data = float(response.text)

print(data)