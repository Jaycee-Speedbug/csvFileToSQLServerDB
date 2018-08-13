#!/usr/bin/python3 
#
#   MapCell
#
#   Classe définissant une carte de jeu WildLife
#

# importe le fichier de constantes
import wildlifeconst


class MapCell:
    """Documentation"""

    _humidity = -1
    _vegetation = -1
    _biome = -1



    def __init__(self,biome,humidity,vegetation):
        """Initialisation d'une cellule de carte"""
        changeHumidity(humidity)
        changeVegetation(vegetation)
        changeBiome(biome)



    def changeHumidity(self,humidity):
        if humidity < 0:
            humidity = 0
        if humidity > 100:
            humidity = 100
        _humidity = humidity



    def changeVegetation(self,vegetation):
        if vegetation < 0:
            vegetation = 0
        if vegetation > 100:
            vegetation = 100
        _vegetation = vegetation



    def changeBiome(self,biome):
        if biome < 0:
            biome = cst.DEFAULT_BIOME
        _biome = biome



