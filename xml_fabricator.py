import xml.etree.ElementTree as ET
import pymongo

root = ET.Element("root")

CONFIG = ET.SubElement(root, "CONFIG").text = "c'est la config qui va contenir l'ip et le port"

SEND = ET.SubElement(root, "SEND")
ET.SubElement(SEND,"ELEMENTS").text="pour les element que le robot peut send"

tree = ET.ElementTree(root)
tree.write("output.xml")

class xml_fabricator:
    def __init__(self):
        pass

    def put_parameters_to_xml(self , DicoOfData): # ici on va créer l'xml à envoyé au robot kuka
        pass


class get_data_for_tweet: # cette classe 

    message = "hellou" # cette variable va contenir le message qui sera tapé par kuka

    def __init__(self) :
        print(self.message)

    @staticmethod
    def set_data_in_variable(sujet):
        client = pymongo.MongoClient("mongodb://localhost:27017/") # je me connecte à la base de donnée
        db = client["DB_Bur_Etude"] # ici je spécifie la base de donnée qui sera utilisé
        collection = db["Collection_Bur_Etude"] # je spécifie aussi la collection qui contient les donnée

        document = collection.find_one({"Sujet": "basic"}) 

        return document

test = get_data_for_tweet.set_data_in_variable(sujet="basic") # c'est un message basique que le robot peut faire
print(test["Description"]) # voila comment on peut avoir la description de ce que le robot va taper sur le clavier