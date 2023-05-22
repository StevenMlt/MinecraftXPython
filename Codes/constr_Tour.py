# Créé par Elève, le 23/02/2021 en Python 3.7

#Permet de construire une tour de blocs.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

for i in range(30):
    mc.setBlock(pos.x+3, pos.y+i, pos.z, 1)

