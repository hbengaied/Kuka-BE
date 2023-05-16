import requests
import random 
import json

# OpenAIRequester permet d'initialisé les variables pour faire une requête openai et elle permet aussi de faire la requête à openai
# class OpenAIRequester:
#     def __init__(self, key):
#         self.key = key
        
#     def make_request(self, prompt):
#         openai.api_key = self.key

#         try:
#             response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)
#             return response
#         except Exception as e:
#             print(f"Une erreur est survenue lors de la requête '{prompt}': {str(e)}")
#             return None

#     @staticmethod
#     def Update_Data_To_DB(url , data):
#         try:
#             client = pymongo.MongoClient(url)
#             db = client["DB_Bur_Etude"]
#             collection = db["collectionChatGPT"]
#             filter_query = {"Topic": "gpt"}
#             update_query = {"$set": {"Topic": "gpt", "Sentence": data}}
#             result = collection.update_one(filter_query, update_query, upsert=True)
#             if result.upserted_id is not None:
#                 print("Nouveau document créé dans MongoDB")
#             else:
#                 print("Document mis à jour dans MongoDB")
#         except Exception as e:
#             print(f"Une erreur est survenue lors de la mise à jour de MongoDB : {str(e)}")
#         finally:
#             client.close()

#         results = collection.insert_one(data)

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

# class MongoDBUpdater:
#     def __init__(self, url):
#         self.url = url

#     def update_pokeApi(self, name, evolution):
#         try:
#             client = pymongo.MongoClient(self.url)
#             db = client["DB_Bur_Etude"]
#             collection = db["collectionPokeAPI"]
#             filter_query = {"Topic": "pokemon"}
#             update_query = {"$set": {"Topic": "pokemon", "Name": name, "Evolves_to": evolution}}
#             result = collection.update_one(filter_query, update_query, upsert=True)
#             if result.upserted_id is not None:
#                 print("Nouveau document créé dans MongoDB")
#             else:
#                 print("Document mis à jour dans MongoDB")
#         except Exception as e:
#             print(f"Une erreur est survenue lors de la mise à jour de MongoDB : {str(e)}")
#         finally:
#             client.close()

# class MongoDbGetData:
    # @staticmethod
    # def get_sentence_hello_world(url): # retourne la phrase basique que kuka doit écrire
    #         client = pymongo.MongoClient(url)
    #         db = client["DB_Bur_Etude"]
    #         collection = db["collectionBasique"]

    #         results = collection.find()

    #         # client.close()

    #         for result in results:
    #             return result["Sentence"]
            
    # @staticmethod
    # def get_sentence_pokemon(url):
    #     client = pymongo.MongoClient(url)
    #     db = client["DB_Bur_Etude"]
    #     collection = db["collectionPokeAPI"]

    #     results = collection.find()

    #     # client.close()

    #     for result in results:
    #         return "wow my " + result["Name"] + " evolve to " + result["Evolves_to"]

    # @staticmethod
    # def get_sentence_GPT(url):
    #     client = pymongo.MongoClient(url)
    #     db = client["DB_Bur_Etude"]
    #     collection = db["collectionChatGPT"]

    #     results = collection.find()

    #     # client.close()

    #     for result in results:
    #         return result["Sentence"]