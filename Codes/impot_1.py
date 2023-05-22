# Créé par Gryfender, le 13/02/2021 en Python 3.7

# Sert à prélever un import quand le joueur est dans une zone.

import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

X1=235
Z1=289
X2=243
Z2=297

ABRI_X=226
ABRI_Y=83
ABRI_Z=293

impot=0
dans_Enclos=0

while True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z<Z2:
        impot+=1
        mc.postToChat("Tu dois la somme de : " + str(impot) + "$")
        dans_Enclos+=1
    else: #Quand joueur en dehors de enclos
        dans_Enclos=0
    if dans_Enclos>3:
        mc.postToChat("Tu es trop lent !")
        mc.player.setPos(ABRI_X, ABRI_Y, ABRI_Z)

