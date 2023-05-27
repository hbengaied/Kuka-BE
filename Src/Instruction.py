import MouseMoveZ as MMZ
import MouveMouseXandY as MMXY
import MovementManager as MM
import VerificationDest as VD
import MouvementXandY as MXY
import MouvementZ as MZ


class InstructionForRobot():
    @staticmethod
    #Cette methode permet de deplacer la souris d'un point A à un Point B et contient les verifications
    #qu'on a bien effectué le mouvement voulu
    def InstructionMouse(lettrePosOuSeTrouveLaSouris, lettrePosOuOnVeutAllerAvecLaSouris):

        #Faire un deplacement en Z en premier vers le haut comme ca si on est au dessus du clavier on monte de +100
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse(lettrePosOuSeTrouveLaSouris)

        #Si le mouvement en Z est ok on fait le mouvement en X et Y pour se trouver au dessus de la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY(lettrePosOuSeTrouveLaSouris, 100)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandYMouse(lettrePosOuSeTrouveLaSouris)
        
        #Si on est au dessus de la souris souris on descend en Z pour se placer dans la souris*
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse(lettrePosOuSeTrouveLaSouris)

        #A partir de ici le bras se trouve dans le trou fait pour la souris
        #donc il faut maintenant la deplacer vers la position voulu

        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True:
            #Faire deplacement en x et y
            if MM.Mouse.MouseXandYCheckBis == False :
                MMXY.MouveMyMouseXandY.MouseMouvementXandY(lettrePosOuOnVeutAllerAvecLaSouris,0)
                MM.Mouse.MouseXandYCheckBis = VD.Verification.VerifXandYMouse(lettrePosOuOnVeutAllerAvecLaSouris)
            
            #Si le deplacement en X et Y a été fait on leve le bras
            if MM.Mouse.MouseXandYCheckBis == True and MM.Mouse.MouseZUpCheckBis == False: 
                MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuOnVeutAllerAvecLaSouris)
                MM.Mouse.MouseZUpCheckBis = VD.Verification.VerifGoUpMouse(lettrePosOuOnVeutAllerAvecLaSouris)

        #Ici si le mouvement voulu a été fait et que le bras c'est relevé on reinitialise tout
        if MM.Mouse.MouseXandYCheckBis == True and MM.Mouse.MouseZUpCheckBis == True :
            MM.Mouse.MouseZUpCheck = False
            MM.Mouse.MouseXandYCheck = False
            MM.Mouse.MouseZDownCheck = False
            MM.Mouse.MouseXandYCheckBis = False
            MM.Mouse.MouseZUpCheckBis = False
            MM.Mouse.EndMouseMouvement = True
            return True

        return False

    #Cette méthode permet de faire un clic gauche, c'est à dire appuyer sur la touche +
    def ClicGauche(lettrePosOuSeTrouveLaSouris):
        #Etape 1 Monter en Z pour Sortir de la souris
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse(lettrePosOuSeTrouveLaSouris)

        #Etape 2 Se diriger vers le bouton +
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY("+", 100)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandYMouse("+")

        #Etape 3 appuyer sur le bouton
        #Si on est au dessus du + on descend en Z pour se placer dans la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown("+")
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse("+")

        #Etape 4 Remonter le bras 
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True and MM.Mouse.MouseZUpCheckBis == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp("+")
            MM.Mouse.MouseZUpCheckBis = VD.Verification.VerifGoUpMouse("+")

        #Ici si le mouvement voulu a été fait et que le bras c'est relevé on reinitialise tout et on return un true 
        if MM.Mouse.MouseZUpCheckBis == True :
            MM.Mouse.MouseZUpCheck = False
            MM.Mouse.MouseXandYCheck = False
            MM.Mouse.MouseZDownCheck = False
            MM.Mouse.MouseXandYCheckBis = False
            MM.Mouse.MouseZUpCheckBis = False
            return True

        return False

    #Cette methode permet de faire au robot écrire sur le clavier, et contient les verifications
    #qu'on a bien effectué le mouvement voulu
    def InstructionClavier():
        if MM.Phrase.Check == False :
                #Je donne les coord au robot en x et y auquel il doit se deplacer
                MXY.MouveMyXandY.MouveXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
                #Si le robot a atteint les coord x et y et set check a true
                MM.Phrase.Check = VD.Verification.VerifXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
            
        #Si le robot à atteint le x et y voulu on va cliquer sur la touche en bougeant le z
        if MM.Phrase.Check == True  and MM.Phrase.CheckDown == False :
            #Deplacement du robot en Z uniquement
            #print("Je descend !!!")
            MZ.MoveMyZ.MoveZDown(MM.Phrase.MyText[MM.Phrase.Compteur])
            MM.Phrase.CheckDown = VD.Verification.VerifKeyClicked(MM.Phrase.MyText[MM.Phrase.Compteur])

        if MM.Phrase.CheckDown == True and MM.Phrase.CheckUp == False :
            # print("Jai pu cliquer sur la touche :", MM.Phrase.MyText[MM.Phrase.Compteur])
            #Ici lorsque la lettre voulu a été cliqué, on va relever l'outil de +75 en Z
            MZ.MoveMyZ.MoveZUp(MM.Phrase.MyText[MM.Phrase.Compteur])
            MM.Phrase.CheckUp = VD.Verification.VerifGoUp(MM.Phrase.MyText[MM.Phrase.Compteur])
            
        #Passage au caractère suivant de la phrase à écrire  
        if MM.Phrase.CheckUp == True and MM.Phrase.Check == True and MM.Phrase.CheckDown == True :
            MM.Phrase.Compteur = MM.Phrase.Compteur +1
            MM.Phrase.Check = False
            MM.Phrase.CheckUp = False
            MM.Phrase.CheckDown = False
            #Ca c'est juste pour eviter un depassement index quand on arrive fin du mot ! Faut impltementer un autre truc plus propre et plus pro 
            if MM.Phrase.Compteur == MM.Phrase.TaillePhrase:
                MM.Phrase.EndText = True
                #ici faire une initialisation
                MM.Mouse.EndMouseMouvement = False
                MM.Mouse.EndMouseMouvementBis = False

    #Cette méthode va permettre d'appuyer sur la touche tabulation afin de nous permettre de tweeter 
    def ClickOnTabulation(lettrePosOuSeTrouveLaSouris, NbOfClicks):
        #Etape 1 Monter en Z pour Sortir de la souris
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse(lettrePosOuSeTrouveLaSouris)

        #Etape 2 Se diriger vers le bouton +
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY("t", 100)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandYMouse("t")

        #Etape 3 appuyer sur le bouton
        #Si on est au dessus du + on descend en Z pour se placer dans la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown("t")
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse("t")

        #Etape 4 Remonter -> Il faut un autre boolen
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True and MM.Mouse.MouseZUpCheckBis == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp("t")
            MM.Mouse.MouseZUpCheckBis = VD.Verification.VerifGoUpMouse("t")

        #Ici si le mouvement voulu a été fait et que le bras c'est relevé on reinitialise tout
        if MM.Mouse.MouseZUpCheckBis == True :
            MM.Mouse.MouseZUpCheck = False
            MM.Mouse.MouseXandYCheck = False
            MM.Mouse.MouseZDownCheck = False
            MM.Mouse.MouseXandYCheckBis = False
            MM.Mouse.MouseZUpCheckBis = False
            MM.Mouse.NombreClickTabulation += 1

        if MM.Mouse.NombreClickTabulation == NbOfClicks :
            MM.Mouse.NombreClickTabulation = 0
            return True

        return False

    #Cette méthode va nous permettre de cliquer sur la touche entrer afin d'envoyer le tweet
    def ClickOnEnter():
        #Etape 1 Monter en Z pour Sortir de la souris
        if MM.Mouse.MouseZUpCheck == False :
            MZ.MoveMyZ.MoveZUp(MM.Phrase.MyText[-1])
            MM.Mouse.MouseZUpCheck= VD.Verification.VerifGoUp(MM.Phrase.MyText[-1])

        #Etape 2 Se diriger vers le bouton +
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY("enter", 100)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandYMouse("enter")

        #Etape 3 appuyer sur le bouton
        #Si on est au dessus de la touche enter on descend en Z pour se placer dans la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown("enter")
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse("enter")

        #Etape 4 Remonter
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True and MM.Mouse.MouseZUpCheckBis == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp("enter")
            MM.Mouse.MouseZUpCheckBis = VD.Verification.VerifGoUpMouse("enter")

        #Ici si le mouvement voulu a été fait et que le bras c'est relevé on reinitialise tout
        if MM.Mouse.MouseZUpCheckBis == True :
            MM.Mouse.MouseZUpCheck = False
            MM.Mouse.MouseXandYCheck = False
            MM.Mouse.MouseZDownCheck = False
            MM.Mouse.MouseXandYCheckBis = False
            MM.Mouse.MouseZUpCheckBis = False
            return True

        return False

    #Cette méthode va cliquer sur la touche N u e fois sur twitter, c'est un raccourci clavier pour
    #ouvrir la zone de tweet
    def OpenWritingSpace() :
        #Etape 1 Monter en Z pour Sortir de la souris
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp("new")
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse("new")

        #Etape 2 Se diriger vers la touche N
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY("new", 100)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandYMouse("new")

        #Etape 3 appuyer sur le bouton
        #Si on est au dessus de N on descend en Z pour se placer dans la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown("new")
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse("new")

        #Etape 4 Remonter
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True and MM.Mouse.MouseZUpCheckBis == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp("new")
            MM.Mouse.MouseZUpCheckBis = VD.Verification.VerifGoUpMouse("new")
            # print("JE REMONTE")

        #Ici si le mouvement voulu a été fait et que le bras c'est relevé on reinitialise tout
        if MM.Mouse.MouseZUpCheckBis == True :
            MM.Mouse.MouseZUpCheck = False
            MM.Mouse.MouseXandYCheck = False
            MM.Mouse.MouseZDownCheck = False
            MM.Mouse.MouseXandYCheckBis = False
            MM.Mouse.MouseZUpCheckBis = False
            return True

        return False


