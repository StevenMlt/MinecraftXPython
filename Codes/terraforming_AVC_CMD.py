# Créé par Elève, le 25/02/2021 en Python 3.7

#Permet de terraformer une zone en la sélectionnant à l'aide de commandes.

import mcpi.event as event
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos=mc.player.getTilePos()


