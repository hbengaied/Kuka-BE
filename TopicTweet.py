import pymongo


class get_data_for_tweet: 

    def __init__(self) :
        pass

    @staticmethod
    def get_data_in_variable(sujet):
        client = pymongo.MongoClient("mongodb://localhost:27017/") # je me connecte à la base de donnée
        db = client["DB_Bur_Etude"] # ici je spécifie la base de donnée qui sera utilisé
        collection = db["Collection_Bur_Etude"] # je spécifie aussi la collection qui contient les donnée

        document = collection.find_one({"Sujet": "basic"}) 

        return document

# test = get_data_for_tweet.set_data_in_variable(sujet="basic") # c'est un message basique que le robot peut faire
# print(test["Description"]) # voila comment on peut avoir la description de ce que le robot va taper sur le clavier
