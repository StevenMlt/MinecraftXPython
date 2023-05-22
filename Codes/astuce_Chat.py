# Créé par Gryfender, le 02/03/2021 en Python 3.7

#Permet d'afficher des astuces dans le Chat à l'aide d'un fichier txt.

import mcpi.minecraft as minecraft
import time
import random

mc = minecraft.Minecraft.create()

NOMDEFICHIER = "astuces.txt"
f = open(NOMDEFICHIER, "r")
astuces = f.readlines()
f.close()
while True:
    time.sleep(random.randint(3,7))
    msg = random.choice(astuces)
    mc.postToChat(msg.strip())

