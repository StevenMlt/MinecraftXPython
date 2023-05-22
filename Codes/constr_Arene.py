# Créé par Gryfender, le 07/03/2021 en Python 3.7

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def constr_Arene(nomdefichier, originex, originey, originez):
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

constr_Arene("Fichiers_CSV/Arene.csv", pos.x-1, pos.y, pos.z-43)