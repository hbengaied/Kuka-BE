import xml.etree.ElementTree as ET
import pymongo

class XmlManager:

    @staticmethod
    def SetDataReceived(DataToPut): # le paramétre DataToPut contient l'xml envoyé par le robot
        with open("input.xml","w") as f:
            f.write(DataToPut)

    @staticmethod
    def GetData(): # cette méthode va me permettre d'obtenir les données du fichier xml

        Tree = ET.parse("input.xml")
        root = Tree.getroot()

        return root

    @staticmethod
    def SetDataToSend(Data): # Data est un dictionnaire qui va contenir tous ce que xml doit contenir 


        # Dans notre cas, les données à envoyé sont les 6 information => X,Y,Z,A,B,C

        root = ET.Element("Sen") # je crée un nouvel élement d'un xml

        root.set("Type" , "ImFree") # j'ajoute l'attribut ImFree au root

        LocToReach = ET.SubElement(root, "Loc")

        LocToReach.set("X" , Data["X"]) # je met les attribut de la balise Loc
        LocToReach.set("Y" , Data["Y"])
        LocToReach.set("Z" , Data["Z"])
        LocToReach.set("A" , Data["A"])
        LocToReach.set("B" , Data["B"])
        LocToReach.set("C" , Data["C"])

        
        TimeStamps = ET.SubElement(root , "IPOC").text = Data["IPOC"] # je crée la balise IPOC
        
        tree = ET.ElementTree(root)
        tree.write("output.xml")


class get_data_for_tweet: 


    def __init__(self) :
        pass

    @staticmethod
    def set_data_in_variable(sujet):
        client = pymongo.MongoClient("mongodb://localhost:27017/") # je me connecte à la base de donnée
        db = client["DB_Bur_Etude"] # ici je spécifie la base de donnée qui sera utilisé
        collection = db["Collection_Bur_Etude"] # je spécifie aussi la collection qui contient les donnée

        document = collection.find_one({"Sujet": "basic"}) 

        return document

# test = get_data_for_tweet.set_data_in_variable(sujet="basic") # c'est un message basique que le robot peut faire
# print(test["Description"]) # voila comment on peut avoir la description de ce que le robot va taper sur le clavier

