# Créé par Gryfender, le 11/02/2021 en Python 3.7

#Permet d'afficher les coordonées du joueur en temps réel et continu.

import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    time.sleep(2)
    pos = mc.player.getTilePos()
    mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
