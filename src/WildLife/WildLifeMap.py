#!/usr/bin/python3 
#
#   Carte de jeu WildLife
#
#   Jaycee
#


from MapCell import MapCell
from wildlifeconst import *


class WildLifeMap:
    """
    Objet modélisant une carte de jeu WildLife
    """



    # Liste des cellules de la carte de jeu
    _cells = []



    # Nom de la carte
    def _get_name(self):
        """getter"""
        return self._name

    def _set_name(self, mapName):
        """setter"""
        self._name = mapName[:MAP_NAME_MAX_LEN]

    name = property(_get_name, _set_name)



    # Largeur de la carte READ ONLY
    @property
    def width(self):
        """getter"""
        return self._width



    # Hauteur de la carte READ ONLY
    @property
    def height(self):
        """getter"""
        return self._height



    def __init__(self, mapName, mapHeight, mapWidth):
        """
        Constructeur de la carte
        Test les caractéristiques fournies pour respecter les normes fixées par constantes
        """

        if mapHeight > MAP_MAX_HEIGHT:
            mapHeight = MAP_MAX_HEIGHT
        self._height = mapHeight

        if mapWidth > MAP_MAX_WIDTH:
            mapWidth = MAP_MAX_WIDTH
        self._width = mapWidth

        self.name = mapName
        
        # Création de la liste contenant toutes les cellules de la carte
        for index in range(1,1 + mapHeight * mapWidth):
            self._cells.append(MapCell(DEFAULT_BIOME, DEFAULT_HUMIDITY, DEFAULT_VEGETATION))



    def mapSize(self):
        """
        Retourne le nombre de cellules dans la carte
        """
        return len(self._cells)



    def addCell(self, x, y, biome, humidity, vegetation):
        """
        Ajoute une cellule à la carte de jeu. En fait, c'est une modification des champs de la cellule à la position (x,y)
        Les coordonnées (x,y) de la cellule commencent à 0
        """
        if x < 0 or x > self._width -1:
            return False
        if y < 0 or y > self._height -1:
            return False
        
        targetCell = self._cells[ x + y * self._width]

        targetCell.biome = biome
        targetCell.humidity = humidity
        targetCell.vegetation = vegetation
        return True



    def getCellAt(self, x, y):
        """
        Retourne une copie de la cellule à la position x,y
        Les coordonnées (x,y) de la cellule commencent à 0
        """
        index = x + y * self._width
        return MapCell(self._cells[index].biome, self._cells[index].humidity, self._cells[index].vegetation)









