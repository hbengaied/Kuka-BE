import openai
import requests
import pymongo
import random 
import json
# OpenAIRequester permet d'initialisé les variables pour faire une requête openai et elle permet aussi de faire la requête à openai
class OpenAIRequester:
    def __init__(self, key):
        self.key = key
        
    def make_request(self, prompt):
        openai.api_key = self.key

        try:
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)
            return response
        except Exception as e:
            print(f"Une erreur est survenue lors de la requête '{prompt}': {str(e)}")
            print("\n je vais donc faire une requete à une api")
            return None

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

class MongoDBUpdater:
    def __init__(self, url):
        self.url = url

    def update_pokeApi(self, name, evolution):
        try:
            client = pymongo.MongoClient(self.url)
            db = client["DB_Bur_Etude"]
            collection = db["collectionPokeAPI"]
            filter_query = {"Topic": "pokemon"}
            update_query = {"$set": {"Topic": "pokemon", "Name": name, "Evolves_to": evolution}}
            result = collection.update_one(filter_query, update_query, upsert=True)
            if result.upserted_id is not None:
                print("Nouveau document créé dans MongoDB")
            else:
                print("Document mis à jour dans MongoDB")
        except Exception as e:
            print(f"Une erreur est survenue lors de la mise à jour de MongoDB : {str(e)}")
        finally:
            client.close()


openAIRequester = OpenAIRequester(key="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")
response = openAIRequester.make_request(prompt="salut")

if(response == None):
    pass

pokeAPIRequester = PokeAPIRequester()
jsonResponse = pokeAPIRequester.make_request()

mongoUpdater = MongoDBUpdater("mongodb://127.0.0.1:27017/")

name = jsonResponse["chain"]["species"]["name"]
evolutions = jsonResponse["chain"]["evolves_to"]

if len(evolutions) > 0:
    mongoUpdater.update_pokeApi(name , evolution = evolutions[0]["species"]["name"] )
else:
    mongoUpdater.update_pokeApi(name , "nothing")