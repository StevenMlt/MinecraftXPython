# Créé par Elève, le 23/02/2021 en Python 3.7

#Permet de construire une maison.

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos=mc.player.getTilePos()

mc.setBlocks(pos.x+3, pos.y-1, pos.z-5, pos.x+14, pos.y+4, pos.z+5, block.COBBLESTONE.id)
mc.setBlocks(pos.x+4, pos.y, pos.z-4, pos.x+13, pos.y+3, pos.z+4, block.AIR.id)
mc.setBlocks(pos.x+4, pos.y-1, pos.z-4, pos.x+13, pos.y-1, pos.z+4, block.WOOD_PLANKS.id)
mc.setBlocks(pos.x+4, pos.y+4, pos.z-4, pos.x+13, pos.y+4, pos.z+4, block.WOOD_PLANKS.id)
mc.setBlocks(pos.x+3, pos.y, pos.z, pos.x+3, pos.y+1, pos.z, block.AIR.id)
mc.setBlocks(pos.x+3, pos.y+1, pos.z-4, pos.x+3, pos.y+1, pos.z-2, block.GLASS_PANE.id)
mc.setBlocks(pos.x+3, pos.y+1, pos.z+2, pos.x+3, pos.y+1, pos.z+4, block.GLASS_PANE.id)