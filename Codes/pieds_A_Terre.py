# Créé par Elève, le 25/02/2021 en Python 3.7

#Permet de savoir si joueur est sur Bloc dur.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def pieds_A_Terre():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z) #Block en dessous coordonées J.
    if b==block.AIR.id or b==block.WATER_STATIONARY.id or b==block.WATER_FLOWING.id:
        mc.postToChat("En Danger !")
    else:
        mc.postToChat("En Securite. ^^")

while True:
    time.sleep(0.5)
    pieds_A_Terre()

