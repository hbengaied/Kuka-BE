import xml.etree.ElementTree as ET
import TopicTweet
import os

class XmlManager:
    @staticmethod
    def SetDataReceived(DataToPut): # le paramétre DataToPut contient l'xml envoyé par le robot
        with open("input.xml","w") as f:
            f.write(DataToPut)

    def DeleteFile():
        chemin_fichier = "output.xml"
        # Vérifier si le fichier existe 
        if os.path.exists(chemin_fichier):
        # Supprimer le fichier
            os.remove(chemin_fichier)
            print("Le fichier a été supprimé avec succès.")
        else:
            print("Le fichier n'existe pas.")

    def GetData(): # cette méthode va me permettre d'obtenir les données du fichier xml

        Tree = ET.parse("input.xml")
        root = Tree.getroot()

        # les principales données qu'on aura besoin est la localisation donc je donne directement la position actuelle du robot
        balise_of_position = root[0]
        attribut_of_this_balsie = balise_of_position.attrib
        locX = attribut_of_this_balsie["X"]

        arrayOfElement = []

        for element in TopicTweet.get_data_for_tweet.get_data_in_variable("basic")["Description"]:
            arrayOfElement.append(element)

        return arrayOfElement

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


