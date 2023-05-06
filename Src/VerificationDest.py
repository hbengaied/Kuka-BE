import xml.etree.ElementTree as ET
import MovementManager as MM


class Verification():
    @staticmethod
    def VerifXandY(lettre):
        try:
            # parse the XML file
            tree = ET.parse('input.xml')

            # get the root element of the XML file
            root = tree.getroot()

            # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 :
                return True
        except:
            pass
        return False

    @staticmethod
    def VerifKeyClicked(lettre):
        try:
        # parse the XML file
            tree = ET.parse('input.xml')

        # get the root element of the XML file
            root = tree.getroot()

        # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"])
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False

    @staticmethod
    def VerifGoUp(lettre):
        try:
            # parse the XML file
            tree = ET.parse('input.xml')

            # get the root element of the XML file
            root = tree.getroot()

            # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"]) + 35
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False

    @staticmethod
    def VerifGoUpMouse(lettre):
        try:
            # parse the XML file
            tree = ET.parse('input.xml')

            # get the root element of the XML file
            root = tree.getroot()

            # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.MouseMouve.MousePos[lettre]["X"])
            PosY = float(MM.MouseMouve.MousePos[lettre]["Y"])
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + 100
            PosA = float(MM.MouseMouve.MousePos[lettre]["A"])
            PosB = float(MM.MouseMouve.MousePos[lettre]["B"])
            PosC = float(MM.MouseMouve.MousePos[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False

    @staticmethod
    def VerifGoDownMouse(lettre):
        try:
        # parse the XML file
            tree = ET.parse('input.xml')

        # get the root element of the XML file
            root = tree.getroot()

        # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.MouseMouve.MousePos[lettre]["X"])
            PosY = float(MM.MouseMouve.MousePos[lettre]["Y"])
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"])
            PosA = float(MM.MouseMouve.MousePos[lettre]["A"])
            PosB = float(MM.MouseMouve.MousePos[lettre]["B"])
            PosC = float(MM.MouseMouve.MousePos[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False