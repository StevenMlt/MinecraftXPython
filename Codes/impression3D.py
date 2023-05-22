# Créé par Gryfender, le 02/03/2021 en Python 3.7

#Permet de créer un block en 3D à l'aide d'un fichier CSV.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

NOMDEFICHIER = "Parcours.csv"

def impression_3D(nomdefichier, originex, originey, originez):
    f = open(nomdefichier, "r")
    lignes = f.readlines()
    coords = lignes[0].split(",")
    dimensionsx = int(coords[0])
    dimensionsy = int(coords[1])
    dimensionsz = int(coords[2])
    idxligne = 1
    for y in range(dimensionsy):
        mc.postToChat(str(y))
        idxligne+=1
        for x in range(dimensionsx):
            ligne = lignes[idxligne]
            idxligne+=1
            donnee = ligne.split(",")
            for z in range(dimensionsz):
                block_ID_DATA = donnee[z]
                list_Block_ID_DATA = block_ID_DATA.split("?")
                mc.setBlock(originex+x, originey+y, originez+z, int(list_Block_ID_DATA[0]), int(list_Block_ID_DATA[1]))

impression_3D(NOMDEFICHIER, pos.x-1, pos.y-1, pos.z-18)
