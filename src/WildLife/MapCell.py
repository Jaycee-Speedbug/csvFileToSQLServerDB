#!/usr/bin/python3 
#
#   MapCell
#
#   Classe définissant une carte de jeu WildLife
#

# importe le fichier de constantes
from wildlifeconst import *


class MapCell:
    """
    Cellule de carte de jeu WildLife
    """



    # Niveau d'humidité de la cellule
    _humidity = -1

    def setHumidity(self, humidity):
        """setter"""
        if humidity < 0:
            humidity = 0
        if humidity > 100:
            humidity = 100
        self._humidity = humidity

    def humidity(self):
        """getter"""
        return self._humidity



    # Niveau de végétation de la cellule
    _vegetation = -1

    def setVegetation(self, vegetation):
        """setter"""
        if vegetation < 0:
            vegetation = 0
        if vegetation > 100:
            vegetation = 100
        self._vegetation = vegetation

    def vegetation(self):
        """getter"""
        return self._vegetation

    # Biome de la cellule
    _biome = -1

    def setBiome(self, biome):
        """setter"""
        if biome < 0:
            biome = DEFAULT_BIOME
        self._biome = biome

    def biome(self):
        """getter"""
        return self._biome



    def __init__(self, biome, humidity, vegetation):
        """
        Construction d'une cellule de carte
        """
        self.setHumidity(humidity)
        self.setVegetation(vegetation)
        self.setBiome(biome)
        



