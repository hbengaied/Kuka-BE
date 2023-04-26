import MovementManager as MM
import ConnectionManager as CM
import xml.etree.ElementTree as ET

class MoveMyZ():
    @staticmethod
    def MoveZDown(lettre):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element

            Data = { # j'initialise le dictionnaire de donnée à envoyé au robot, ATTENTION 
                "X" : MM.Dictionnarie.Dico[lettre]["X"],
                "Y" : MM.Dictionnarie.Dico[lettre]["Y"],
                "Z" : MM.Dictionnarie.Dico[lettre]["Z"], 
                "A" : MM.Dictionnarie.Dico[lettre]["A"],
                "B" : MM.Dictionnarie.Dico[lettre]["B"],
                "C" : MM.Dictionnarie.Dico[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data) # cette fonction sert à initialisé le fichier xml "output.xml"
            CM.SendData.Send() # et juste aprés, il envoie le fichier xml
            
        except:
            pass

    @staticmethod
    def MoveZUp(lettre):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"]) + 75
            StringPosZ = str(PosZ)
            Data = { # j'initialise le dictionnaire de donnée à envoyé au robot, ATTENTION 
                "X" : MM.Dictionnarie.Dico[lettre]["X"],
                "Y" : MM.Dictionnarie.Dico[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.Dictionnarie.Dico[lettre]["A"],
                "B" : MM.Dictionnarie.Dico[lettre]["B"],
                "C" : MM.Dictionnarie.Dico[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data) # cette fonction sert à initialisé le fichier xml "output.xml"
            CM.SendData.Send() # et juste aprés, il envoie le fichier xml
            
        except:
            pass