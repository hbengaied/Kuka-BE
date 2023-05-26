import MovementManager as MM
import ConnectionManager as CM
import XmlManager
import xml.etree.ElementTree as ET

class MouveMyMouseXandY():
    @staticmethod
    #Si on veut que la souris aille à la position originale on lui donnera la lettre a
    # sinon pour l'endroit ou le boutton publier se trouve envoyer la touche b
    # Methode qui permet de déplacer la souris en X et en Y uniquement
    #Cette méthode prend en arguement une "lettre" qui est la position de la où se trouve la souris.
    #La variable monint, lui correspond à la hauteur en Z du bras, car cette méthode sert à 2 choses,
    #aller à la souris et la déplacer d'un point A à un point B
    def MouseMouvementXandY(lettre, monint):
        try:
            tree = ET.parse("input.xml")
            root = tree.getroot()

            ipoc_balise = ""
            for element in root:
                if element.tag == "IPOC":
                    ipoc_balise = element
            
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + monint
            StringPosZ = str(PosZ)
            Data = {
                "X" : MM.MouseMouve.MousePos[lettre]["X"],
                "Y" : MM.MouseMouve.MousePos[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.MouseMouve.MousePos[lettre]["A"],
                "B" : MM.MouseMouve.MousePos[lettre]["B"],
                "C" : MM.MouseMouve.MousePos[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data)
            CM.SendData.Send()
            
        except:
            pass
