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
    def _set_humidity(self, humidity):
        """setter"""
        if humidity < 0:
            humidity = 0
        if humidity > 100:
            humidity = 100
        self._humidity = humidity

    def _get_humidity(self):
        """getter"""
        return self._humidity

    humidity = property(_get_humidity, _set_humidity)



    # Niveau de végétation de la cellule
    def _set_vegetation(self, vegetation):
        """setter"""
        if vegetation < 0:
            vegetation = 0
        if vegetation > 100:
            vegetation = 100
        self._vegetation = vegetation

    def _get_vegetation(self):
        """getter"""
        return self._vegetation

    vegetation = property(_get_vegetation, _set_vegetation)



    # Biome de la cellule
    def _set_biome(self, biome):
        """setter"""
        if biome < 0:
            biome = DEFAULT_BIOME
        self._biome = biome

    def _get_biome(self):
        """getter"""
        return self._biome

    biomeDbID = property(_get_biome, _set_biome)



    def __init__(self, biome, humidity, vegetation):
        """
        Construction d'une cellule de carte
        """
        self.humidity = humidity
        self.vegetation = vegetation
        self.biome = biome
        



