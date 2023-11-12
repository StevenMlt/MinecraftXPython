# Minecraft x Python

## Description

Projet de 1ère (Lycée) réalisé en Python sur Minecraft à l'aide de l'API <strong>mcpi</strong> et d'un serveur Bukkit (vers. 1.6.4.).

Le but du projet était de pouvoir copier une structure composée de blocks dans Minecraft, et de pouvoir la reproduire n'importe où dans le monde du jeu et autant qu'on le voulait. 
N'ayant pratiquement jamais programmé avant d'entreprendre ce projet, le code est très amateur et brouillon, je n'avais alors que quelques connaissances d'algorithmique et en Python. J'ai été très guidé, 
notamment grâce au livre <strong>"Adventures in Minecraft"</strong> de <strong>David Whale</strong> et <strong>Martin O'Hanlon</strong>, mais ce projet m'a permis d'avoir une première approche du monde 
de l'informatique et de la programmation, et m'aura donné du fil à retordre et de nombreux problèmes à résoudre. Cela aura été très instructif.

Le code et la structure du dossier ont été laissés tels-quels depuis la fin du projet.

## Fonctionnement

Le fonctionnement est assez simple, on utilise des commandes et fonctions de l'API pour "scanner" la zone voulue en récupérant block par block, l'identifiant et la variante des blocks qui composent la zone préalablement 
définie. Ces données sont stockées dans un Tableur (fichier .csv) représentant la structure de la zone, vue du dessus et couche par couche. Un peu comme la structure d'un immeuble, l'immeuble représente la zone et chaque 
étage est composé de différentes pièces/appartements, dans notre cas nous affichons les étages vus du dessus et côte à côte. Les informations des blocks sont stockées dans chacune des cellules qui composent un étage de 
la zone sous la forme du couple "identifiant?variante" (? étant un séparateur).

Une fois la zone scannée et les informations stockées, on n'a plus qu'à lire le fichier et, à l'aide de méthodes, replacer les blocks et cela autant de fois qu'on le veux.
