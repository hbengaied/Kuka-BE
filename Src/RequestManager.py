import requests
import random 
import json

class PokeAPIRequester:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/evolution-chain/"

    def make_request(self):
        number = str(random.randint(1,539)) # je prend un chiffre random qui fait lien vers un pokemon
        try:
            response = requests.get(self.url + number)
            if response.status_code == 200: # Si je recois une bonne réponse
                return json.loads(response.text)
        except Exception as e:
            print(f"Une erreur est survenue lors de la requête vers l'API PokéAPI : {str(e)}")
            return None

    def give_me_sentence(self):
        jsonResponse = self.make_request()

        name = jsonResponse["chain"]["species"]["name"]
        evolutions = jsonResponse["chain"]["evolves_to"]

        if len(evolutions) > 0:
            phrase = "wow my " + name + " evolve to " + evolutions[0]["species"]["name"]
            return phrase
            # mongoUpdater.update_pokeApi(name , evolution = evolutions[0]["species"]["name"] )
        else:
            phrase = "wow my " + name + " evolve to nothing"
            return phrase

