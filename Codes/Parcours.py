# Créé par Gryfender, le 06/03/2021 en Python 3.7

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

X = 100.5 #pos x du centre de l'Arène
Y = 80    #pos y du centre de l'Arène
Z = 250.5 #pos z du centre de l'Arène
POS_CENTRE_ARENE = (100.5, 80, 250.5)

def reset_Arene_Centrale(nomdefichier, originex, originey, originez):
    mc.setBlocks(X-17, Y+1, Z-17, X+17, Y+30,Z+17, 0)
    f = open(nomdefichier, "r")
    lignes = f.readlines()
    coords = lignes[0].split(",")
    dimensionsx = int(coords[0])
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        mc.postToChat(str(y))  #Possiblement à enlever
        idxligne+=1
        for x in range(dimensionsx):
            ligne = lignes[idxligne]
            idxligne+=1
            donnee = ligne.split(",")
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))

def constr_Parcours(nomdefichier, originex, originey, originez):
    f = open(nomdefichier, "r")
    lignes = f.readlines()
    coords = lignes[0].split(",")
    dimensionsx = int(coords[0])
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        mc.postToChat(str(y))  #Possiblement à enlever
        idxligne+=1
        for x in range(dimensionsx):
            ligne = lignes[idxligne]
            idxligne+=1
            donnee = ligne.split(",")
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))

reset_Arene_Centrale("Fichiers_CSV/Reset_Arene.csv", pos.x-1, pos.y-2, pos.z-18)
constr_Parcours("Fichiers_CSV/Parcours.csv", pos.x-1, pos.y-1, pos.z-18)
constr_Parcours("Fichiers_CSV/Parcours.csv", pos.x-1, pos.y-1, pos.z-18)

while True:
    time.sleep(1.5)
    mc.setBlocks(X-6,Y+17,Z+1,X-7,Y+17,Z+2,0,0)
    time.sleep(1.5)
    mc.setBlocks(X-6,Y+17,Z+1,X-7,Y+17,Z+2,126,12)






