#!/usr/bin/python3 
#
#   CellBiome
#
#   Classe définissant un biome s'appliquant à une cellule de carte de jeu WildLife
#




class CellBiome(object):
    """
    Biome d'une cellule MapCell de carte de jeu WildLife

    La propriété databaseID est en lecture seule
    """


    # ID du biome dans la base de données READ ONLY
    @property
    def databaseID(self):
        """setter"""
        return self._databaseID
    


    # Nom du biome
    def set_biomeName(self, name):
        """setter"""
        self._biomeName = name

    def get_biomeName(self):
        """getter"""
        return self._biomeName

    biomeName = property(get_biomeName, set_biomeName)



    # Humidité du biome
    def set_humidity(self, humidity):
        """setter"""
        self._humidity = humidity

    def get_humidity(self):
        """getter"""
        return self._humidity

    humidity = property(get_humidity, set_humidity)



    # Niveau de végétation du biome
    def set_vegetation(self, vegetation):
        """setter"""
        self._vegetation = vegetation

    def get_vegetation(self):
        """getter"""
        return self._vegetation

    vegetation = property(get_vegetation, set_vegetation)



    def __init__(self, dbID, name, humidity, vegetation):
        """
        Construction d'un biome s'appliquant à une cellule de carte de jeu WildLife
        """
        self._databaseID = dbID
        self.biomeName = name
        self.humidity = humidity
        self.vegetation = vegetation


    


    

