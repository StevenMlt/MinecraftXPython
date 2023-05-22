# Créé par Elève, le 23/02/2021 en Python 3.7

#Permet de construire une maison.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

DIMENSIONS=20
pos=mc.player.getTilePos()
x=pos.x+2
y=pos.y
z=pos.z
midx=x+DIMENSIONS/2
midy=y+DIMENSIONS/2

mc.setBlocks(x, y, z, x+DIMENSIONS, y+DIMENSIONS, z+DIMENSIONS, block.COBBLESTONE.id)
mc.setBlocks(x+1, y, z+1, x+DIMENSIONS-2, y+DIMENSIONS-1, z+DIMENSIONS-2, block.AIR.id)
mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

mc.setBlocks(x+3, y+DIMENSIONS-3, z, midx-3, midy+3, z, block.GLASS.id)
mc.setBlocks(midx+3, y+DIMENSIONS-3, z, x+DIMENSIONS-3, midy+3, z, block.GLASS.id)
mc.setBlocks(x, y+DIMENSIONS-1, z, x+DIMENSIONS, y+DIMENSIONS-1, z+DIMENSIONS, block.WOOD.id)
mc.setBlocks(x+1, y-1, z+1, x+DIMENSIONS-2, y-1, z+DIMENSIONS-2, block.WOOL.id, 14)