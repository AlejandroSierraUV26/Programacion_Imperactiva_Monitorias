import requests 
import json

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
