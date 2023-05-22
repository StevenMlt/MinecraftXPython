# Créé par Gryfender, le 02/03/2021 en Python 3.7

#Permet de scanner une structure 3D et de la sauvegarder dans un fichier CSV.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

NOMDEFICHIER = "arbre.csv"

#Dimensions de la structure devant être scannée.
DIMENSIONSX = 5
DIMENSIONSY = 5
DIMENSIONSZ = 5

def scan_3D(nomdefichier, originex, originey, originez):
    f = open(nomdefichier, "w")
    f.write(str(DIMENSIONSX) + "," + str(DIMENSIONSY) + "," + str(DIMENSIONSZ) + "\n")
    for y in range(DIMENSIONSY):
        f.write("\n")
        for x in range(DIMENSIONSX):
            line = ""
            for z in range(DIMENSIONSZ):
                blockid = mc.getBlock(originex+x, originey+y, originez+z)
                if line != "":
                    line = line + ","
                line = line + str(blockid)
            f.write(line + "\n")
        f.close()

scan_3D(NOMDEFICHIER, pos.x-(DIMENSIONSX/2), pos.y, pos.z-(DIMENSIONSZ/2))