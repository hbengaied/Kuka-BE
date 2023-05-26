import MovementManager as MM
import ConnectionManager as CM
import XmlManager
import xml.etree.ElementTree as ET

class MouveMyXandY():
    # Methode qui permet de déplacer le bras en X et en Y uniquement
    #Cette méthode prend en arguement une lettre qui qui correspond à la position de la lettre sur le clavier.
    #On peut voir que on ajoute toujours +35 au Z de la position afin que le robot ait une marge de sécurité avec
    #le clavier lors du déplacement
    @staticmethod
    def MouveXandY(lettre):
        try:
            tree = ET.parse("input.xml")
            root = tree.getroot()
            ipoc_balise = ""
            for element in root:
                if element.tag == "IPOC":
                    ipoc_balise = element
            
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"]) + 35
            StringPosZ = str(PosZ)
            Data = { 
                "X" : MM.Dictionnarie.Dico[lettre]["X"],
                "Y" : MM.Dictionnarie.Dico[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.Dictionnarie.Dico[lettre]["A"],
                "B" : MM.Dictionnarie.Dico[lettre]["B"],
                "C" : MM.Dictionnarie.Dico[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data)
            CM.SendData.Send()
            
        except:
            pass
