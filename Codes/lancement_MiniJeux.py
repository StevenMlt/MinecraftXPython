# Créé par Gryfender, le 08/03/2021 en Python 3.7

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os
mc = minecraft.Minecraft.create()

#Coordonnées temporaires block centre Arène
X= -105
Y= 80
Z= 250

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



#Définition ID + Data du block de laine
ID_DATA_BLANC = "Block(35, 0)"
ID_DATA_ORANGE = "Block(35, 1)"
ID_DATA_ROSE = "Block(35, 2)"
ID_DATA_JAUNE = "Block(35, 4)"
ID_DATA_VERT = "Block(35, 5)"
ID_DATA_ROUGE = "Block(35, 14)"
ID_DATA_NOIR = "Block(35, 15)"
ID_DATA_BLEU = "Block(35, 3)"

def verif_Block_Blanc(x,y,z):
    block_Laine = "Block(35, 0)"
    verif_Block = str(mc.getBlockWithData(x,y,z))
    print(verif_Block)
    if verif_Block != block_Laine:
        mc.postToChat("Block Blanc casse")

verif_Block_Blanc(X_Violet_Blanc,Y_Violet_Blanc,Z_Violet_Blanc)
