#!/usr/bin/python3 
#
#   MapCell
#
#   Classe définissant une carte de jeu WildLife
#

# importe le fichier de constantes
from wildlifeconst import *


class MapCell:
    """Documentation"""

    _humidity = -1
    _vegetation = -1
    _biome = -1



    def humidity(self, humidity):
        if humidity < 0:
            humidity = 0
        if humidity > 100:
            humidity = 100
        self._humidity = humidity



    def vegetation(self, vegetation):
        if vegetation < 0:
            vegetation = 0
        if vegetation > 100:
            vegetation = 100
        self._vegetation = vegetation



    def biome(self, biome):
        if biome < 0:
            biome = DEFAULT_BIOME
        self._biome = biome



    def __init__(self, biome, humidity, vegetation):
        """Initialisation d'une cellule de carte"""
        self.humidity(humidity)
        self.vegetation(vegetation)
        self.biome(biome)
        



