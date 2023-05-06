import MouseMoveZ as MMZ
import MouveMouseXandY as MMXY
import MovementManager as MM
import VerificationDest as VD

#declarer les bool dans un autre fichier apres,
# mais mtn comme j'eris en blind je fais le code et apres j'ameliore


class Instruction():
    @staticmethod
    #Cette methode permet de deplacer la souris d'un point A à un Point B et contient les verification
    #qu'on a bien effectué le mouvement voulu
    def InstructionMouseMouve(lettrePosOuSeTrouveLaSouris, lettrePosOuOnVeutAllerAvecLaSouris):
        #Faire un deplacement en Z en premier vers le haut comme ca si on est au dessus du clavier on monte de +100
        if MM.Mouse.MouseZUpCheck == False :
            MMZ.MoveMyMouseZ.MoveMouseZUp(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZUpCheck = VD.Verification.VerifGoUpMouse(lettrePosOuSeTrouveLaSouris)

        #Si le mouvement en Z est ok on fait le mouvement en X et Y de la souris
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == False:
            MMXY.MouveMyMouseXandY.MouseMouvementXandY(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseXandYCheck = VD.Verification.VerifXandY(lettrePosOuSeTrouveLaSouris)
        
        if MM.Mouse.MouseZUpCheck == True and MM.Mouse.MouseXandYCheck == True and MM.Mouse.MouseZDownCheck == False:
            MMZ.MoveMyMouseZ.MoveMouseZDown(lettrePosOuSeTrouveLaSouris)
            MM.Mouse.MouseZDownCheck = VD.Verification.VerifGoDownMouse(lettrePosOuSeTrouveLaSouris)

        #A partir de ici le bras se trouve dans le trouve fait pour la souris
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