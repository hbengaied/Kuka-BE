import MouseMoveZ as MMZ
import MouveMouseXandY as MMXY
import MovementManager as MM
import VerificationDest as VD
import MouvementXandY as MXY
import MouvementZ as MZ

#declarer les bool dans un autre fichier apres,
# mais mtn comme j'eris en blind je fais le code et apres j'ameliore


class InstructionForRobot():
    @staticmethod
    #Cette methode permet de deplacer la souris d'un point A à un Point B et contient les verification
    #qu'on a bien effectué le mouvement voulu
    def InstructionMouse(lettrePosOuSeTrouveLaSouris, lettrePosOuOnVeutAllerAvecLaSouris):

        #Faire un deplacement en Z en premier vers le haut comme ca si on est au dessus du clavier on monte de +100
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse(lettrePosOuSeTrouveLaSouris)

        #Si le mouvement en Z est ok on fait le mouvement en X et Y pour se trouver au dessus de la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandY(lettrePosOuSeTrouveLaSouris)
        
        #Si on est au dessus de la souris souris on descend en Z pour se placer dans la souris*
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse(lettrePosOuSeTrouveLaSouris)

        #A partir de ici le bras se trouve dans le trou fait pour la souris
        #donc il faut maintenant la deplacer vers la position voulu

        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == True:
            #Faire deplacement en x et y
            if MM.Mouse.MouseXandYCheckBis == False :
                MMXY.MouveMyMouseXandY.MouseMouvementXandY(lettrePosOuOnVeutAllerAvecLaSouris)
                MM.Mouse.MouseXandYCheckBis = VD.Verification.VerifXandY(lettrePosOuOnVeutAllerAvecLaSouris)
            
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



    def InstructionClavier():
        if MM.Phrase.Check == False :
                #Je donne les coord au robot en x et y auquel il doit se deplacer
                MXY.MouveMyXandY.MouveXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
                #Si le robot a atteint les coord x et y et set check a true
                MM.Phrase.Check = VD.Verification.VerifXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
            
        #Si le robot à atteint le x et y voulu on va cliquer sur la touche en bougeant le z
        if MM.Phrase.Check == True  and MM.Phrase.CheckDown == False :
            #Deplacement du robot en Z uniquement
            print("Je descend !!!")
            MZ.MoveMyZ.MoveZDown(MM.Phrase.MyText[MM.Phrase.Compteur])
            MM.Phrase.CheckDown = VD.Verification.VerifKeyClicked(MM.Phrase.MyText[MM.Phrase.Compteur])

        if MM.Phrase.CheckDown == True and MM.Phrase.CheckUp == False :
            # print("Jai pu cliquer sur la touche :", MM.Phrase.MyText[MM.Phrase.Compteur])
            #Ici lorsque la lettre voulu a été cliqué, on va relever l'outil de +75 en Z
            MZ.MoveMyZ.MoveZUp(MM.Phrase.MyText[MM.Phrase.Compteur])
            MM.Phrase.CheckUp = VD.Verification.VerifGoUp(MM.Phrase.MyText[MM.Phrase.Compteur])
            
            #Je vais passer caractere suivant    
        if MM.Phrase.CheckUp == True and MM.Phrase.Check == True and MM.Phrase.CheckDown == True :
            print("On incremente le compteur ")
            MM.Phrase.Compteur = MM.Phrase.Compteur +1
            MM.Phrase.Check = False
            MM.Phrase.CheckUp = False
            MM.Phrase.CheckDown = False
            #Ca c'est juste pour eviter un depassement index quand on arrive fin du mot ! Faut impltementer un autre truc plus propre et plus pro 
            if MM.Phrase.Compteur == MM.Phrase.TaillePhrase:
                print("On vient de finir la phrase maintenant passer au deplacement de la souris")
                MM.Phrase.EndText = True
                #ici faire une initialisation
                MM.Mouse.EndMouseMouvement = False
                MM.Mouse.EndMouseMouvementBis = False