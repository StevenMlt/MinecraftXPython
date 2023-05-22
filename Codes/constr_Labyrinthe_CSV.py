# Créé par Gryfender, le 02/03/2021 en Python 3.7

#Permet de construire un labyrinthe à partir d'un fichier CSV.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

ESPACE = block.AIR.id
MUR = block.WOOD.id
SOL = block.COBBLESTONE.id

NOMDEFICHIER = "labyrinthe1.csv"
f = open(NOMDEFICHIER, "r")

ORIGINE_X = pos.x+1
ORIGINE_Y = pos.y+1
ORIGINE_Z = pos.z+1
z = ORIGINE_Z

for line in f.readlines():
    data = line.split(",")
    x = ORIGINE_X
    for cell in data:
        if cell == "0":
            b = ESPACE
        else:
            b = MUR
        mc.setBlock(x, ORIGINE_Y, z, b)
        mc.setBlock(x, ORIGINE_Y+1, z, b)
        mc.setBlock(x, ORIGINE_Y-1, z, SOL)
        x+=1
    z+=1
