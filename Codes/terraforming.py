# Créé par Elève, le 23/02/2021 en Python 3.7

#Permet de changer les blocks d'une zone 3D définie rapidement.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()

pos=mc.player.getTilePos()
dimensions=int(input("Dimensions de l'espace à déblayer ?"))

mc.setBlocks(pos.x-dimensions, pos.y, pos.z-dimensions, pos.x+dimensions, pos.y+dimensions, pos.z+dimensions, 0)