# Créé par Gryfender, le 07/03/2021 en Python 3.7

import mcpi.minecraft as minecraft  #Importation des modules nécessaires au programme.
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()   #Création de la liaison entre le serveur Minecraft et Python.
pos = mc.player.getTilePos()    #Obtention de la position du joueur au lancement du programme

#On définit d'abord toutes les fonctions qui seront utiles pour le programme avant de les utiliser dans le programme principal.



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



def constr_Arene(nomdefichier, originex, originey, originez):  #Fonction de construction de l'Arène avec un fichier CSV.
    mc.postToChat("Attendre...")        #Le fichier est un tableau csv de données contenant les id et data des blocks composants
    f = open(nomdefichier, "r")         #   l'Arène, le principe est que cette fonction va parcourir chaque cellule de chaque ligne
    lignes = f.readlines()              #   composants le tableau, va récupérer les valeurs stockées dedans et placer un block avec
    coords = lignes[0].split(",")       #   ces caractéristiques à chaque cellule qu'il rencontre. Il y a dans ce tableau des groupes
    dimensionsx = int(coords[0])        #   de lignes représentants les couches de la structure, 1er groupe = couche 1, etc.
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        """mc.postToChat(str(y)) #Utile pour dev mais pas pour jeu."""  #Affiche dans le chat les couches qui ont été construites.
        idxligne+=1
        for x in range(dimensionsx):        #L'id et la data d'un block sont séparées d'un "?", sous la forme donc "28?3". On récupère
            ligne = lignes[idxligne]        #   cette donnée sous une chaîne de caractère qui ne peut pas être utilisée en l'état, nous
            idxligne+=1                     #   la transformons en liste avec pour séparateur le caractère "?" ce qui nous donne les
            donnee = ligne.split(",")       #   2 paramètres nécessaires pour placer un block, l'id(28) et la data(3).
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))
    mc.postToChat("C'est bon.")

#Détermination du point central de l'Arène par rapport à la position du Joueur à la création de la structure, block de sable au centre du cercle.
X = pos.x+44 #pos x du centre de l'Arène
Y = pos.y+9  #pos y du centre de l'Arène
Z = pos.z    #pos z du centre de l'Arène
POS_CENTRE_ARENE = (X,Y,Z)



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



def explication_Blocks_MiniJeux(): #Fonction pour envoyer un message d'explication quand le Joueur se trouve dans 1 des 4 zones de départ.
    global message_Ecrit1
    global message_Ecrit2
    global message_Ecrit3
    global message_Ecrit4
    global zoneViolette_OCCUPEE
    global zoneVerte_OCCUPEE
    global zoneBlanche_OCCUPEE
    global zoneRouge_OCCUPEE

    pos = mc.player.getTilePos() #Obtenir la position du Joueur.

    X1_1= X-28      #Coordonnées de la zone Violette.
    X1_2= X-23
    Z1_1= Z-4
    Z1_2= Z+4
    Y1_1= Y+1
    Y1_2= Y+4

    X2_1= X+4      #Coordonnées de la zone Verte.
    X2_2= X-4
    Z2_1= Z-28
    Z2_2= Z-23
    Y2_1= Y+2
    Y2_2= Y+4

    X3_1= X+28      #Coordonnées de la zone Blanche.
    X3_2= X+23
    Z3_1= Z+4
    Z3_2= Z-4
    Y3_1= Y+2
    Y3_2= Y+4

    X4_1= X-4      #Coordonnées de la zone Rouge.
    X4_2= X+4
    Z4_1= Z+28
    Z4_2= Z+23
    Y4_1= Y+2
    Y4_2= Y+4

    #Définition du message d'explication sous forme de liste pour le faire apparaître ligne par ligne dans le chat.
    message_Explication = ["Pour executer un MiniJeu cassez un block de laine de la couleur correspondante : ","Blanc   = Jeu de Parcours","Orange = MiniJeu 2","Rose    = MiniJeu 3","Jaune  = MiniJeu 4","Vert    = MiniJeu 5","Rouge  = MiniJeu 6","Noir     = MiniJeu 7","Bleu    = MiniJeu 8"]
    time.sleep(0.50)  #Intervalle de rafraichissement

    if pos.x<=X1_2 and pos.x>=X1_1 and pos.y<=Y1_2 and pos.y>=Y1_1 and pos.z<=Z1_2 and pos.z>=Z1_1 and message_Ecrit1==False: #Si joueur dans zone Violette et que le message n'a pas été écrit(anti-spam)
        mc.postToChat(message_Explication[0]) #Mettre le message dans le Chat.
        time.sleep(0.5)                       #Temps de pause qui rends l'arrivée du message moins aggressive.
        mc.postToChat(message_Explication[1])
        mc.postToChat(message_Explication[2])
        mc.postToChat(message_Explication[3])
        mc.postToChat(message_Explication[4])
        mc.postToChat(message_Explication[5])
        mc.postToChat(message_Explication[6])
        mc.postToChat(message_Explication[7])
        mc.postToChat(message_Explication[8])
        message_Ecrit1=True #Le message a été écrit
        zoneViolette_OCCUPEE = True #Le joueur est dans la zone
    elif pos.x>X1_2 or pos.x<X1_1 or pos.y>Y1_2 or pos.z>Z1_2 or pos.z<Z1_1: #Si Joueur en dehors de zone:
        message_Ecrit1=False #Le message n'a pas été écrit
        zoneViolette_OCCUPEE = False #Le joueur n'est pas dans la zone

    if pos.x>=X2_2 and pos.x<=X2_1 and pos.y<=Y2_2 and pos.y>=Y2_1 and pos.z<=Z2_2 and pos.z>=Z2_1 and message_Ecrit2==False: #Si joueur dans zone Verte et que le message n'a pas été écrit(anti-spam)
        mc.postToChat(message_Explication[0]) #Mettre le message dans le Chat.
        time.sleep(0.5)                       #Temps de pause qui rends l'arrivée du message moins aggressive.
        mc.postToChat(message_Explication[1])
        mc.postToChat(message_Explication[2])
        mc.postToChat(message_Explication[3])
        mc.postToChat(message_Explication[4])
        mc.postToChat(message_Explication[5])
        mc.postToChat(message_Explication[6])
        mc.postToChat(message_Explication[7])
        mc.postToChat(message_Explication[8])
        message_Ecrit2=True #Le message a été écrit
        zoneVerte_OCCUPEE = True #Le joueur est dans la zone
    elif pos.x<X2_2 or pos.x>X2_1 or pos.y>Y2_2 or pos.z>Z2_2 or pos.z<Z2_1: #Si Joueur en dehors de zone:
        message_Ecrit2=False #Le message n'a pas été écrit
        zoneVerte_OCCUPEE = False #Le joueur n'est pas dans la zone

    if pos.x>=X3_2 and pos.x<=X3_1 and pos.y<=Y3_2 and pos.y>=Y3_1 and pos.z>=Z3_2 and pos.z<=Z3_1 and message_Ecrit3==False: #Si joueur dans zone Blanche et que le message n'a pas été écrit(anti-spam)
        mc.postToChat(message_Explication[0]) #Mettre le message dans le Chat.
        time.sleep(0.5)                       #Temps de pause qui rends l'arrivée du message moins aggressive.
        mc.postToChat(message_Explication[1])
        mc.postToChat(message_Explication[2])
        mc.postToChat(message_Explication[3])
        mc.postToChat(message_Explication[4])
        mc.postToChat(message_Explication[5])
        mc.postToChat(message_Explication[6])
        mc.postToChat(message_Explication[7])
        mc.postToChat(message_Explication[8])
        message_Ecrit3=True #Le message a été écrit
        zoneBlanche_OCCUPEE = True #Le joueur est dans la zone
    elif pos.x<X3_2 or pos.x>X3_1 or pos.y>Y3_2 or pos.z<Z3_2 or pos.z>Z3_1: #Si Joueur en dehors de zone:
        message_Ecrit3=False #Le message n'a pas été écrit
        zoneBlanche_OCCUPEE = False #Le joueur n'est pas dans la zone

    if pos.x<=X4_2 and pos.x>=X4_1 and pos.y<=Y4_2 and pos.y>=Y4_1 and pos.z>=Z4_2 and pos.z<=Z4_1 and message_Ecrit4==False: #Si joueur dans zone Rouge et que le message n'a pas été écrit(anti-spam)
        mc.postToChat(message_Explication[0]) #Mettre le message dans le Chat.
        time.sleep(0.5)                       #Temps de pause qui rends l'arrivée du message moins aggressive.
        mc.postToChat(message_Explication[1])
        mc.postToChat(message_Explication[2])
        mc.postToChat(message_Explication[3])
        mc.postToChat(message_Explication[4])
        mc.postToChat(message_Explication[5])
        mc.postToChat(message_Explication[6])
        mc.postToChat(message_Explication[7])
        mc.postToChat(message_Explication[8])
        message_Ecrit4=True #Le message a été écrit
        zoneRouge_OCCUPEE = True #Le joueur est dans la zone
    elif pos.x>X4_2 or pos.x<X4_1 or pos.y>Y4_2 or pos.z<Z4_2 or pos.z>Z4_1: #Si Joueur en dehors de zone:
        message_Ecrit4=False #Le message n'a pas été écrit
        zoneRouge_OCCUPEE = False #Le joueur n'est pas dans la zone



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Ensemble de fonctions permettant de détecter quand un block de laine est cassé dans une des zones de départ, ce qui changera la valeur d'un booléen
#   qui permettra le lancement du MiniJeu correspondant au block cassé.

#Définition des coordonnées des blocks de laine par rapport au centre de l'Arène ( X,Y,Z ).

#Coordonées x,y,z du block de laine blanche dans zone Violette
X_Violet_Blanc = X-27
Y_Violet_Blanc = Y+3
Z_Violet_Blanc = Z-4
#Coordonées x,y,z du block de laine orange dans zone Violette
X_Violet_Orange = X-26
Y_Violet_Orange = Y+3
Z_Violet_Orange = Z-4
#Coordonées x,y,z du block de laine rose dans zone Violette
X_Violet_Rose = X-25
Y_Violet_Rose = Y+3
Z_Violet_Rose = Z-4
#Coordonées x,y,z du block de laine jaune dans zone Violette
X_Violet_Jaune = X-24
Y_Violet_Jaune = Y+3
Z_Violet_Jaune = Z-4
#Coordonées x,y,z du block de laine verte dans zone Violette
X_Violet_Vert = X-24
Y_Violet_Vert = Y+3
Z_Violet_Vert = Z+4
#Coordonées x,y,z du block de laine rouge dans zone Violette
X_Violet_Rouge = X-25
Y_Violet_Rouge = Y+3
Z_Violet_Rouge = Z+4
#Coordonées x,y,z du block de laine noir dans zone Violette
X_Violet_Noir = X-26
Y_Violet_Noir = Y+3
Z_Violet_Noir = Z+4
#Coordonées x,y,z du block de laine bleue dans zone Violette
X_Violet_Bleu = X-27
Y_Violet_Bleu = Y+3
Z_Violet_Bleu = Z+4


#Coordonées x,y,z du block de laine blanche dans zone Verte
X_Vert_Blanc = X+4
Y_Vert_Blanc = Y+3
Z_Vert_Blanc = Z-27
#Coordonées x,y,z du block de laine orange dans zone Verte
X_Vert_Orange = X+4
Y_Vert_Orange = Y+3
Z_Vert_Orange = Z-26
#Coordonées x,y,z du block de laine rose dans zone Verte
X_Vert_Rose = X+4
Y_Vert_Rose = Y+3
Z_Vert_Rose = Z-25
#Coordonées x,y,z du block de laine jaune dans zone Verte
X_Vert_Jaune = X+4
Y_Vert_Jaune = Y+3
Z_Vert_Jaune = Z-24
#Coordonées x,y,z du block de laine verte dans zone Verte
X_Vert_Vert = X-4
Y_Vert_Vert = Y+3
Z_Vert_Vert = Z-24
#Coordonées x,y,z du block de laine rouge dans zone Verte
X_Vert_Rouge = X-4
Y_Vert_Rouge = Y+3
Z_Vert_Rouge = Z-25
#Coordonées x,y,z du block de laine noir dans zone Verte
X_Vert_Noir = X-4
Y_Vert_Noir = Y+3
Z_Vert_Noir = Z-26
#Coordonées x,y,z du block de laine bleue dans zone Verte
X_Vert_Bleu = X-4
Y_Vert_Bleu = Y+3
Z_Vert_Bleu = Z-27


#Coordonées x,y,z du block de laine blanche dans zone Blanche
X_Blanc_Blanc = X+27
Y_Blanc_Blanc = Y+3
Z_Blanc_Blanc = Z+4
#Coordonées x,y,z du block de laine orange dans zone Blanche
X_Blanc_Orange = X+26
Y_Blanc_Orange = Y+3
Z_Blanc_Orange = Z+4
#Coordonées x,y,z du block de laine rose dans zone Blanche
X_Blanc_Rose = X+25
Y_Blanc_Rose = Y+3
Z_Blanc_Rose = Z+4
#Coordonées x,y,z du block de laine jaune dans zone Blanche
X_Blanc_Jaune = X+24
Y_Blanc_Jaune = Y+3
Z_Blanc_Jaune = Z+4
#Coordonées x,y,z du block de laine verte dans zone Blanche
X_Blanc_Vert = X+24
Y_Blanc_Vert = Y+3
Z_Blanc_Vert = Z-4
#Coordonées x,y,z du block de laine rouge dans zone Blanche
X_Blanc_Rouge = X+25
Y_Blanc_Rouge = Y+3
Z_Blanc_Rouge = Z-4
#Coordonées x,y,z du block de laine noir dans zone Blanche
X_Blanc_Noir = X+26
Y_Blanc_Noir = Y+3
Z_Blanc_Noir = Z-4
#Coordonées x,y,z du block de laine bleue dans zone Blanche
X_Blanc_Bleu = X+27
Y_Blanc_Bleu = Y+3
Z_Blanc_Bleu = Z-4


#Coordonées x,y,z du block de laine blanche dans zone Rouge
X_Rouge_Blanc = X-4
Y_Rouge_Blanc = Y+3
Z_Rouge_Blanc = Z+27
#Coordonées x,y,z du block de laine orange dans zone Rouge
X_Rouge_Orange = X-4
Y_Rouge_Orange = Y+3
Z_Rouge_Orange = Z+26
#Coordonées x,y,z du block de laine rose dans zone Rouge
X_Rouge_Rose = X-4
Y_Rouge_Rose = Y+3
Z_Rouge_Rose = Z+25
#Coordonées x,y,z du block de laine jaune dans zone Rouge
X_Rouge_Jaune = X-4
Y_Rouge_Jaune = Y+3
Z_Rouge_Jaune = Z+24
#Coordonées x,y,z du block de laine verte dans zone Rouge
X_Rouge_Vert = X+4
Y_Rouge_Vert = Y+3
Z_Rouge_Vert = Z+24
#Coordonées x,y,z du block de laine rouge dans zone Rouge
X_Rouge_Rouge = X+4
Y_Rouge_Rouge = Y+3
Z_Rouge_Rouge = Z+25
#Coordonées x,y,z du block de laine noir dans zone Rouge
X_Rouge_Noir = X+4
Y_Rouge_Noir = Y+3
Z_Rouge_Noir = Z+26
#Coordonées x,y,z du block de laine bleue dans zone Rouge
X_Rouge_Bleu = X+4
Y_Rouge_Bleu = Y+3
Z_Rouge_Bleu = Z+27


"""
ID + Data du block de laine
ID_DATA_BLANC = "Block(35, 0)"
ID_DATA_ORANGE = "Block(35, 1)"
ID_DATA_ROSE = "Block(35, 2)"
ID_DATA_JAUNE = "Block(35, 4)"
ID_DATA_VERT = "Block(35, 5)"
ID_DATA_ROUGE = "Block(35, 14)"
ID_DATA_NOIR = "Block(35, 15)"
ID_DATA_BLEU = "Block(35, 3)"
"""

#Définition des fonctions détectant si un block est cassé ou non, on va simplement vérifier l'id/data du block à
#   la position précédemment définie, si c'est la même alors le block n'a pas été cassé, en revanche si celle
#   récupérée est "0,0" celà correspont au block d'air et donc le block de laine a été cassé et remplacé par
#   "de l'air" littéralement.

def verif_Block_Blanc(x,y,z):
    global miniJeu_EnCours
    global miniJeu_Parcours_Lance
    block_Laine = "Block(35, 0)"                    #Définition de l'id/data du block de laine.
    verif_Block = str(mc.getBlockWithData(x,y,z))   #Définition d'une variable associée à la commande pour récupérer l'id/data d'un block.
    if verif_Block != block_Laine:                  #Si les 2 données ne sont pas les même alors:
        mc.setBlock(x,y,z,35,0)                     #   on remet le block où il devrait être et on change les valeurs des bolléens.
        miniJeu_EnCours = True
        miniJeu_Parcours_Lance = True

def verif_Block_Orange(x,y,z):                      #C'est la même chose pour tous les blocks.
    global miniJeu_EnCours
    global miniJeu_2_Lance
    block_Laine = "Block(35, 1)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,1)
        miniJeu_EnCours = True
        miniJeu_2_Lance = True

def verif_Block_Rose(x,y,z):
    global miniJeu_EnCours
    global miniJeu_3_Lance
    block_Laine = "Block(35, 2)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,2)
        miniJeu_EnCours = True
        miniJeu_3_Lance = True

def verif_Block_Jaune(x,y,z):
    global miniJeu_EnCours
    global miniJeu_4_Lance
    block_Laine = "Block(35, 4)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,4)
        miniJeu_EnCours = True
        miniJeu_4_Lance = True

def verif_Block_Vert(x,y,z):
    global miniJeu_EnCours
    global miniJeu_5_Lance
    block_Laine = "Block(35, 5)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,5)
        miniJeu_EnCours = True
        miniJeu_5_Lance = True

def verif_Block_Rouge(x,y,z):
    global miniJeu_EnCours
    global miniJeu_6_Lance
    block_Laine = "Block(35, 14)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,14)
        miniJeu_EnCours = True
        miniJeu_6_Lance = True

def verif_Block_Noir(x,y,z):
    global miniJeu_EnCours
    global miniJeu_7_Lance
    block_Laine = "Block(35, 15)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,15)
        miniJeu_EnCours = True
        miniJeu_7_Lance = True

def verif_Block_Bleu(x,y,z):
    global miniJeu_EnCours
    global miniJeu_8_Lance
    block_Laine = "Block(35, 3)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    if verif_Block != block_Laine:
        mc.setBlock(x,y,z,35,3)
        miniJeu_EnCours = True
        miniJeu_8_Lance = True

def blocks_Lancement_MiniJeux_Violet():                                 #On regroupe les fonctions par zone.
    verif_Block_Blanc(X_Violet_Blanc,Y_Violet_Blanc,Z_Violet_Blanc)
    verif_Block_Orange(X_Violet_Orange,Y_Violet_Orange,Z_Violet_Orange)
    verif_Block_Rose(X_Violet_Rose,Y_Violet_Rose,Z_Violet_Rose)
    verif_Block_Jaune(X_Violet_Jaune,Y_Violet_Jaune,Z_Violet_Jaune)
    verif_Block_Vert(X_Violet_Vert,Y_Violet_Vert,Z_Violet_Vert)
    verif_Block_Rouge(X_Violet_Rouge,Y_Violet_Rouge,Z_Violet_Rouge)
    verif_Block_Noir(X_Violet_Noir,Y_Violet_Noir,Z_Violet_Noir)
    verif_Block_Bleu(X_Violet_Bleu,Y_Violet_Bleu,Z_Violet_Bleu)

def blocks_Lancement_MiniJeux_Vert():
    verif_Block_Blanc(X_Vert_Blanc,Y_Vert_Blanc,Z_Vert_Blanc)
    verif_Block_Orange(X_Vert_Orange,Y_Vert_Orange,Z_Vert_Orange)
    verif_Block_Rose(X_Vert_Rose,Y_Vert_Rose,Z_Vert_Rose)
    verif_Block_Jaune(X_Vert_Jaune,Y_Vert_Jaune,Z_Vert_Jaune)
    verif_Block_Vert(X_Vert_Vert,Y_Vert_Vert,Z_Vert_Vert)
    verif_Block_Rouge(X_Vert_Rouge,Y_Vert_Rouge,Z_Vert_Rouge)
    verif_Block_Noir(X_Vert_Noir,Y_Vert_Noir,Z_Vert_Noir)
    verif_Block_Bleu(X_Vert_Bleu,Y_Vert_Bleu,Z_Vert_Bleu)

def blocks_Lancement_MiniJeux_Blanc():
    verif_Block_Blanc(X_Blanc_Blanc,Y_Blanc_Blanc,Z_Blanc_Blanc)
    verif_Block_Orange(X_Blanc_Orange,Y_Blanc_Orange,Z_Blanc_Orange)
    verif_Block_Rose(X_Blanc_Rose,Y_Blanc_Rose,Z_Blanc_Rose)
    verif_Block_Jaune(X_Blanc_Jaune,Y_Blanc_Jaune,Z_Blanc_Jaune)
    verif_Block_Vert(X_Blanc_Vert,Y_Blanc_Vert,Z_Blanc_Vert)
    verif_Block_Rouge(X_Blanc_Rouge,Y_Blanc_Rouge,Z_Blanc_Rouge)
    verif_Block_Noir(X_Blanc_Noir,Y_Blanc_Noir,Z_Blanc_Noir)
    verif_Block_Bleu(X_Blanc_Bleu,Y_Blanc_Bleu,Z_Blanc_Bleu)

def blocks_Lancement_MiniJeux_Rouge():
    verif_Block_Blanc(X_Rouge_Blanc,Y_Rouge_Blanc,Z_Rouge_Blanc)
    verif_Block_Orange(X_Rouge_Orange,Y_Rouge_Orange,Z_Rouge_Orange)
    verif_Block_Rose(X_Rouge_Rose,Y_Rouge_Rose,Z_Rouge_Rose)
    verif_Block_Jaune(X_Rouge_Jaune,Y_Rouge_Jaune,Z_Rouge_Jaune)
    verif_Block_Vert(X_Rouge_Vert,Y_Rouge_Vert,Z_Rouge_Vert)
    verif_Block_Rouge(X_Rouge_Rouge,Y_Rouge_Rouge,Z_Rouge_Rouge)
    verif_Block_Noir(X_Rouge_Noir,Y_Rouge_Noir,Z_Rouge_Noir)
    verif_Block_Bleu(X_Rouge_Bleu,Y_Rouge_Bleu,Z_Rouge_Bleu)



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Fonction servant à nettoyer l'Arène, souvent lors de l'arrêt ou au lancement d'un MiniJeu.

def reset_Arene_Centrale(nomdefichier, originex, originey, originez):
    global arene_Reset
    mc.setBlocks(X-18, Y+1, Z-18, X+18, Y+30,Z+18, 0)       #Cuve de lave pour détruire les items.
    mc.setBlocks(X-19, Y, Z-19, X+19, Y,Z+19, 20,0)         #
    mc.setBlocks(X-19, Y+1, Z-19, X+19, Y+1,Z+19, 20,0)     #
    mc.setBlocks(X-18, Y+1, Z-18, X+18, Y+1,Z+18, 11,0)     #
    time.sleep(3.5)
    mc.setBlocks(X-19, Y, Z-19, X+19, Y+1,Z+19, 0)      #Enlèvement de la cuve de lave. On remplace tout par des blocks d'air.
    f = open(nomdefichier, "r")                         #Ici on réutilise le même programme que pour la construction de l'Arène
    lignes = f.readlines()                              #   mais cette fois juste pour le centre de la structure si elle a été
    coords = lignes[0].split(",")                       #   détruite ou modifiée.
    dimensionsx = int(coords[0])
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        """mc.postToChat(str(y))  #Utile pour dev mais pas pour jeu."""
        idxligne+=1
        for x in range(dimensionsx):
            ligne = lignes[idxligne]
            idxligne+=1
            donnee = ligne.split(",")
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Fonction servant tout comme la construction de l'Arène à recréer une structure, ici celle du MiniJeu de parcours.

def constr_Parcours(nomdefichier, originex, originey, originez):
    global parcours_Construit
    f = open(nomdefichier, "r")
    lignes = f.readlines()
    coords = lignes[0].split(",")
    dimensionsx = int(coords[0])
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        """mc.postToChat(str(y))  #Utile pour dev mais pas pour jeu."""
        idxligne+=1
        for x in range(dimensionsx):
            ligne = lignes[idxligne]
            idxligne+=1
            donnee = ligne.split(",")
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Fonction intervenant pour le lancement d'un MiniJeu et l'explication de son arrêt.

def lancement_MiniJeu(fichiercsvminijeu):
    global parcours_Construit
    global miniJeu_EnCours
    global arene_Vide
    global block_Leave_Construit
    miniJeu_EnCours = True
    mc.postToChat("Attendre...")
    reset_Arene_Centrale(fichiercsvminijeu, X-18, Y-1, Z-18)    #Fonction pour nettoyer l'Arène centrale.
    mc.player.setPos(X-16.5,Y+1,Z+0.5)                          #Téléportation du Joueur sur l'Arène centrale.
    constr_Parcours("Parcours.csv", X-18, Y, Z-18) #Construction du MiniJeu de parcours.
    parcours_Construit = parcours_Construit + 1
    arene_Vide = False
    constr_Parcours("Parcours.csv", X-18, Y, Z-18) #2e construction, certains blocks se placent mal lors de la 1ère.
    parcours_Construit = parcours_Construit + 1
    mc.postToChat("Construction terminee.")
    time.sleep(0.25)
    mc.postToChat("Activite lancee ^^")
    time.sleep(0.25)
    mc.postToChat("Pour quitter le MiniJeu cassez le block de laine blanche au niveau de la zone Violette")
    mc.setBlock(X-18,Y+2,Z, 35, 0) #Création du block de retour, au niveau de la zone Violette sur l'Arène centrale, si cassé alors le MiniJeu s'arrête.
    block_Leave_Construit = True



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Fonction d'arrêt d'un MiniJeu, c'est à dire quand le block de retour est cassé.

def arret_MiniJeu():
    global miniJeu_EnCours
    global arene_Vide
    global parcours_Construit
    global block_Leave_Construit
    global miniJeu_Parcours_Lance
    global miniJeu_2_Lance
    global miniJeu_3_Lance
    global miniJeu_4_Lance
    global miniJeu_5_Lance
    global miniJeu_6_Lance
    global miniJeu_7_Lance
    global miniJeu_8_Lance
    mc.player.setPos(X-31.5,Y+2.3,Z+0.5)                                    #Téléportation du Joueur sur les bords de l'Arène.
    reset_Arene_Centrale("Reset_Arene.csv", X-18, Y-1, Z-18)   #Reset de l'Arène centrale.
    miniJeu_EnCours = False
    miniJeu_Parcours_Lance = False
    miniJeu_2_Lance = False
    miniJeu_3_Lance = False
    miniJeu_4_Lance = False
    miniJeu_5_Lance = False
    miniJeu_6_Lance = False
    miniJeu_7_Lance = False
    miniJeu_8_Lance = False
    arene_Vide = True
    parcours_Construit = 0
    block_Leave_Construit = False



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



def  message_Win_MiniJeu_Parcours(): #Met un message de félicitations quand le Joueur arrive à la fin du MiniJeu parcours.
    global message_Win_MiniJeu_Parcours_Ecrit
    x1 = X+1        #Définition des coordonnées des 2 angles opposés définissants la zone d'arrivée.
    x2 = X+7
    y1 = Y+26
    y2 = Y+29
    z1 = Z-7
    z2 = Z-1
    pos = mc.player.getPos()    #On récupère la position du Joueur.
    #Si le Joueur est dans la zone alors :
    if pos.x >= x1 and pos.x <= x2 and pos.y >= y1 and pos.y <= y2 and pos.z >= z1 and pos.z <= z2 and message_Win_MiniJeu_Parcours_Ecrit == False:
        mc.postToChat("Bien joue ! Tu as termine le parcours, les recompenses sont a toi ! Tu peux refaire le parcours ou quitter en cassant le block de laine blanche en bas.")
        message_Win_MiniJeu_Parcours_Ecrit = True
    #Si le Joueur est en dehors de la zone alors :
    elif pos.x < x1 or pos.x > x2 or pos.y < y1 or pos.y > y2 or pos.z < z1 or pos.z > z2:
        message_Win_MiniJeu_Parcours_Ecrit = False



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



#Fonction servant à renvoyer le Joueur sur les murailles quand il saute/tombe dans les douves ou le renvoyer sur l'Arène en fonction
#   du MiniJeu (si jeu principe d'élimination renvoie sur muraille).

def douves_Interdites():
    x1 = X-30               #Encore une fois définition des limites de la zone.
    x2 = X+30
    y1 = Y-1
    y2 = Y-7
    z1 = Z-30
    z2 = Z+30
    pos = mc.player.getPos() #Position du Joueur
    #Si le Joueur tombe dans les douves.
    if pos.x >= x1 and pos.x <= x2 and pos.y >= y2 and pos.y <= y1 and pos.z >= z1 and pos.z <= z2:
        if miniJeu_Parcours_Lance == True:          #Et que c'est le MiniJeu de parcours qui est lancé alors on le renvoie sur l'Arène centrale.
            mc.player.setPos(X-16.5,Y+1,Z+0.5)
        elif miniJeu_2_Lance == True:               #Si ce sont les autres MiniJeux, on le renvoie sur les murailles.
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_3_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_4_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_5_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_6_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_7_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_8_Lance == True:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)
        elif miniJeu_EnCours == False:
            mc.player.setPos(X-31.5,Y+2.3,Z+0.5)



######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



# /!\ Programme Principal utilisant toutes les fonctions.

constr_Arene("Arene.csv", pos.x+1, pos.y, pos.z-43) #Construction de l'Arène.

mc.postToChat("Bienvenue dans l'Arene, pour lancer un Mini-Jeu allez dans une des zones colorees au plus proche de l'Arene.") #Message de bienvenue.

#Définition de toutes les variables.

zoneViolette_OCCUPEE = False  #Initialisation des variables d'occupation d'une zone. False = non, True = oui.
zoneVerte_OCCUPEE = False
zoneBlanche_OCCUPEE = False
zoneRouge_OCCUPEE = False

message_Ecrit1=False #Initialisation des variables de vérification d'envoie des messages d'explication des MiniJeux. False = non, True = oui.
message_Ecrit2=False
message_Ecrit3=False
message_Ecrit4=False

miniJeu_EnCours = False #Variable pour savoir si un MiniJeu est en cours. False = non, True = oui.
miniJeu_Parcours_Lance = False #Variable pour savoir si les MiniJeux sont actifs. False = non, True = oui.
miniJeu_2_Lance = False
miniJeu_3_Lance = False
miniJeu_4_Lance = False
miniJeu_5_Lance = False
miniJeu_6_Lance = False
miniJeu_7_Lance = False
miniJeu_8_Lance = False

arene_Vide = True #Variable pour savoir si l'Arène centrale est vide ou non. False = non, True = oui.
parcours_Construit = 0 #Variable pour savoir si le parcours a été construit et combien de fois. 2fois pour être sûr que tous les blocks aient bien été placés.

block_Leave_Construit = False #Variable montrant si le block de retour est en place ou non. False = non, True = oui.
block_Laine_Leave = "Block(35, 0)" #Variable représentant l'ID et la Data du block de laine de retour.
verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z)) #Variable de vérification d'ID et de Data du block aux coordonnées.

while True:         #Programme qui tourne en boucle.


    douves_Interdites()         #Fonction téléportant le Joueur si il tombe dans les douves.



    if miniJeu_EnCours == False:
        explication_Blocks_MiniJeux() #Message dans le chat d'explication des MiniJeux quand rien n'est en cours et que le joueur entre dans 1 des 4 zones.

    if zoneViolette_OCCUPEE == True and miniJeu_EnCours == False: #Vérification de la sélection du block de MiniJeu en fonction de la Zone, placement du Joueur sur l'Arène et création du block de retour.
        blocks_Lancement_MiniJeux_Violet()

    if zoneVerte_OCCUPEE == True and miniJeu_EnCours == False: #Vérification de la sélection du block de MiniJeu en fonction de la Zone, placement du Joueur sur l'Arène et création du block de retour.
        blocks_Lancement_MiniJeux_Vert()

    if zoneBlanche_OCCUPEE == True and miniJeu_EnCours == False: #Vérification de la sélection du block de MiniJeu en fonction de la Zone, placement du Joueur sur l'Arène et création du block de retour.
        blocks_Lancement_MiniJeux_Blanc()

    if zoneRouge_OCCUPEE == True and miniJeu_EnCours == False: #Vérification de la sélection du block de MiniJeu en fonction de la Zone, placement du Joueur sur l'Arène et création du block de retour.
        blocks_Lancement_MiniJeux_Rouge()



    if miniJeu_Parcours_Lance == True and arene_Vide == True and parcours_Construit < 2: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        message_Win_MiniJeu_Parcours_Ecrit = False              #Le message de félicitations en étant arrivé à la fin du MiniJeu n'a pas été écrit.
        lancement_MiniJeu("Reset_Arene.csv")       #Reset de l'Arène centrale.
        while miniJeu_Parcours_Lance == True:                   #Si le MiniJeu de parcours a été lancé :
            message_Win_MiniJeu_Parcours()                      #Fonction de message de félicitations.
            douves_Interdites()                                 #Fonction interdisant les douves.
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))  #Vérification du block de retour.
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:  #Si le block de retour est cassé, le MiniJeu s'arrête
                arret_MiniJeu()
            time.sleep(1.5)                                 #Obstacle du parcours apparaissant et disparraissant toute les 1s et demie.
            mc.setBlocks(X-6,Y+17,Z+1,X-7,Y+17,Z+2,126,12)
            time.sleep(1.5)
            mc.setBlocks(X-6,Y+17,Z+1,X-7,Y+17,Z+2,0,0)



    #C'est le même principe pour chaque MiniJeu.

    if miniJeu_2_Lance == True and arene_Vide == True:
        mc.postToChat("Le MiniJeu 2 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_2_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 2 a ete arrete.")



    if miniJeu_3_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 3 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_3_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 3 a ete arrete.")



    if miniJeu_4_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 4 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_4_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 4 a ete arrete.")



    if miniJeu_5_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 5 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_5_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 5 a ete arrete.")



    if miniJeu_6_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 6 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_6_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 6 a ete arrete.")



    if miniJeu_7_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 7 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_7_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 7 a ete arrete.")



    if miniJeu_8_Lance == True and arene_Vide == True: #Si un block de MiniJeu a été cassé le MiniJeu associé est lancé.
        mc.postToChat("Le MiniJeu 8 a ete lance.")
        miniJeu_EnCours = True
        arene_Vide = False
        block_Leave_Construit = True
        while miniJeu_8_Lance == True:
            verif_Block_Leave = str(mc.getBlockWithData(X-18,Y+2,Z))
            if miniJeu_EnCours == True and arene_Vide == False and block_Leave_Construit == True and verif_Block_Leave != block_Laine_Leave:
                arret_MiniJeu()
                mc.postToChat("Le MiniJeu 8 a ete arrete.")

#Fin du programme.