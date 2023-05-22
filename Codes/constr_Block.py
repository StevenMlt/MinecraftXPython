# Créé par Elève, le 23/02/2021 en Python 3.7

# Permet de placer automatiquement un block

import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

POSITION= pos.x+3, pos.y, pos.z
mc.setBlock(POSITION, block.DIRT.id)

