# Créé par Gryfender, le 11/02/2021 en Python 3.7

#Module servant à tester des codes sans les sauvegarder.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def fonction_Test():
    pos = mc.player.getTilePos()
    block = mc.getBlockWithData(pos.x, pos.y-1, pos.z)
    print(block)





