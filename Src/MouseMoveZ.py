import MovementManager as MM
import ConnectionManager as CM
import xml.etree.ElementTree as ET
import XmlManager

class MoveMyMouseZ():
    @staticmethod
    def MoveMouseZDown(lettre):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element

            Data = { # j'initialise le dictionnaire de donnée à envoyé au robot, ATTENTION 
                "X" : MM.MouseMouve.MousePos[lettre]["X"],
                "Y" : MM.MouseMouve.MousePos[lettre]["Y"],
                "Z" : MM.MouseMouve.MousePos[lettre]["Z"], 
                "A" : MM.MouseMouve.MousePos[lettre]["A"],
                "B" : MM.MouseMouve.MousePos[lettre]["B"],
                "C" : MM.MouseMouve.MousePos[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data) # cette fonction sert à initialisé le fichier xml "output.xml"
            CM.SendData.Send() # et juste aprés, il envoie le fichier xml
        except:
            pass

    @staticmethod
    def MoveMouseZUp(lettre):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + 100
            StringPosZ = str(PosZ)
            Data = { # j'initialise le dictionnaire de donnée à envoyé au robot, ATTENTION 
                "X" : MM.MouseMouve.MousePos[lettre]["X"],
                "Y" : MM.MouseMouve.MousePos[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.MouseMouve.MousePos[lettre]["A"],
                "B" : MM.MouseMouve.MousePos[lettre]["B"],
                "C" : MM.MouseMouve.MousePos[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data) # cette fonction sert à initialisé le fichier xml "output.xml"
            CM.SendData.Send() # et juste aprés, il envoie le fichier xml
            
        except:
            pass