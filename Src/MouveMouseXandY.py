import MovementManager as MM
import ConnectionManager as CM
import XmlManager
import xml.etree.ElementTree as ET

class MouveMyMouseXandY():
    @staticmethod
    #Si on veut que la souris aille à la position originale on lui donnera la lettre a
    # sinon pour l'endroit ou le boutton publier se trouve envoyer la touche b
    def MouseMouvementXandY(lettre, monint):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element
            
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + monint
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
