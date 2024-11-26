# Necesito toda la informacion de los pokemones apartir de esta api: https://pokeapi.co/api/v2/pokemon/ditto


import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for i in data['abilities']:
        print(i['ability']['name'])
        
else:
    print("Error en la request")
    

