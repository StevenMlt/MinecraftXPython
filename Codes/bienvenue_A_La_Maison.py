# Créé par Gryfender, le 11/02/2021 en Python 3.7

#Permet de dire bienvenue 1fois quand joueur passe dans zone définie.

import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

X1=197 #Coordonnées de la zone.
X2=201
Z1=268
Z2=272
Y1=106

message_Ecrit=0 #Variable qui permet de savoir si le message a été envoyé: 0=non 1=oui

while True: #Boucle qui fait tourner le programme en permanence
    time.sleep(0.25)  #Intervalle de rafraichissement
    pos = mc.player.getTilePos()
    if pos.x<=X2 and pos.x>=X1 and pos.y==Y1 and pos.z<=Z2 and pos.z>=Z1 and message_Ecrit==0: #Si joueur dans zone:
        mc.postToChat("Bienvenue a la maison") #Mettre le message dans le Chat.
        message_Ecrit=1
    elif pos.x>X2 or pos.x<X1 or pos.z>Z2 or pos.z<Z1: #Si Joueur en dehors de zone:
        message_Ecrit=0

