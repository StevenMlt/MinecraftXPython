# Créé par Gryfender, le 08/02/2021 en Python 3.7

#Permet d'afficher les coordonées du joueur.

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
