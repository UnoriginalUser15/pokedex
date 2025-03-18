import pandas as pd
import requests
import json



# calls the api and loads data into json
def search(search_input):

    type_response = requests.get("https://pokeapi.co/api/v2/type").json()
    type_list = []
    # iterates through the type_response and makes a list of types
    for type_dict in type_response['results']:
        type_list.append(type_dict['name'])

    # searches for the type and loads into json
    if search_input in type_list:
        url = "https://pokeapi.co/api/v2/type/" + search_input
        response = requests.get(url)

        # checks that there is actually a respone from the pokeapi
        if response.status_code == 200:
            type_data = json.dumps(response.json(), indent=4)

            # writes data about searched type to a json file
            with open("src/data/type_data.json", "w") as type_json:
                type_json.write(type_data)

        else:
            print(f"Error: {response}")
        
        return "type"

    # searches for pokemon based on ID or name
    else:
        url = "https://pokeapi.co/api/v2/pokemon/" + search_input
        response = requests.get(url)

        # checks that there is actually a respone from the pokeapi
        if response.status_code == 200:
            pokemon_data = json.dumps(response.json(), indent=4)

            # writes data about searched pokemon to a json file
            with open("src/data/poke_data.json", "w") as poke_json:
                poke_json.write(pokemon_data)
        elif response.status_code == 404:
            print(f"Error: Pokémon does not exist (404 Error)")

        return "pokemon"
