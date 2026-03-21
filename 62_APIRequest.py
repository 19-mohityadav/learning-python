# Requesting API using Python

import requests


base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        pokemon_info = response.json()
        # print("Data Received")
        return pokemon_info
    else:
        print(f"Data Not Received--> {response.status_code}")
        return response.status_code

pokemon_name = "pikachu"
# get_pokemon_info(pokemon_name)
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"ID: {pokemon_info['id']} and Name: {pokemon_info['name']}")
