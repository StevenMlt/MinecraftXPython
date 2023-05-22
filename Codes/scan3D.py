import mcpi.minecraft as minecraft
import mcpi.block as block

# Module pour utiliser les expressions régulières
import re

# Module pour utiliser la fonction time
import time

mc = minecraft.Minecraft.create()

FILENAME = "Fichiers_CSV/Reset_Arene.csv"
SIZEX = 37
SIZEY = 3
SIZEZ = 37

def scan3D(filename, originx, originy, originz):
  f = open(filename, "w")
  f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
  for y in range(SIZEY):
    f.write("\n")
    for x in range(SIZEX):
      line = ""
      for z in range(SIZEZ):
        block_ID_DATA = str(mc.getBlockWithData(originx+x, originy+y, originz+z))
        char_Non_Voulu = "Block() "
        char_Remplace = ","
        for char in char_Non_Voulu:
            block_ID_DATA = block_ID_DATA.replace(char,"")
        for char in char_Remplace:
            block_ID_DATA = block_ID_DATA.replace(char,"?")
        if line != "":
          line = line + ","
        line = line + str(block_ID_DATA)
      f.write(line + "\n")
  f.close()

def scan3DJo(filename, originx, originy, originz):
  f = open(filename, "w")
  f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
  for y in range(SIZEY):
    f.write("\n")
    for x in range(SIZEX):
      line = ""
      for z in range(SIZEZ):
        block_ID_DATA = str(mc.getBlockWithData(originx+x, originy+y, originz+z))

        # Ne récupère que les chiffres entre parenthèses sous la forme d'un tableau
        block_ID_DATA = re.findall(r'[0-9]+', block_ID_DATA)

        # Concatène les deux premières valeurs du tableau sous la forme N?M
        reste = (block_ID_DATA[0] + "?" + block_ID_DATA[1])

        #reste = str(block_ID_DATA)

        if line != "":
          line = line + ","
        line = line + reste
      f.write(line + "\n")
  f.close()

pos = mc.player.getTilePos()

t0= time.clock()

#scan3D(FILENAME, pos.x-(SIZEX/2), pos.y, pos.z-(SIZEZ/2))
scan3DJo(FILENAME, pos.x-(SIZEX/2), pos.y, pos.z-(SIZEZ/2))

t1 = time.clock() - t0
print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)



