# Créé par Gryfender, le 03/03/2021 en Python 3.7

#A utiliser en regardant le Nord, créer un cadrillage devant et à gauche de 400 blocks sur 400 avec des carrés de 50 blocks de côté.

import mcpi.event as event
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

b = 89  #id du block de remplissage.
v = 0  #data du block de remplissage.

#Création du cadrillage ligne par ligne.

mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x, pos.y-1, pos.z-200 ,b,v) #1
mc.setBlocks(pos.x-50, pos.y-1, pos.z, pos.x-50, pos.y-1, pos.z-200 ,b,v) #2
mc.setBlocks(pos.x-100, pos.y-1, pos.z, pos.x-100, pos.y-1, pos.z-200 ,b,v) #3
mc.setBlocks(pos.x-150, pos.y-1, pos.z, pos.x-150, pos.y-1, pos.z-200 ,b,v) #4
mc.setBlocks(pos.x-200, pos.y-1, pos.z, pos.x-200, pos.y-1, pos.z-200 ,b,v) #5

mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x-200, pos.y-1, pos.z ,b,v) #1
mc.setBlocks(pos.x, pos.y-1, pos.z-50, pos.x-200, pos.y-1, pos.z-50 ,b,v) #2
mc.setBlocks(pos.x, pos.y-1, pos.z-100, pos.x-200, pos.y-1, pos.z-100 ,b,v) #3
mc.setBlocks(pos.x, pos.y-1, pos.z-150, pos.x-200, pos.y-1, pos.z-150 ,b,v) #4
mc.setBlocks(pos.x, pos.y-1, pos.z-200, pos.x-200, pos.y-1, pos.z-200 ,b,v) #5



