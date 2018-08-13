#!/usr/bin/python3 
#
#   Carte de jeu WildLife
#
#   Jaycee
#


from MapCell import *


class WildLifeMap:
    """Carte de jeu WildLife"""

    _cells[0:0] = MapCell(0,0,0,0)
    _height = -1
    _width = -1
    _name = ""



    def __init__(self,mapName,mapHeight,mapWidth):
        _height = mapHeight
        _width = mapWidth
        _name = mapName



    def addCell(self,x,y,biome,humidity,vegetation):
        if x < 0 or x > _width -1:
            return False
        if y < 0 or y > _height -1:
            return False
        cells[x:y] = MapCell(biome,humidity,vegetation)
        return True



    def getCellAt(x,y):
        """Return a copy of the Cell at position x,y"""
        return MapCell(_cells[x:y].biome,_cells[x:y].humidity,_cells[x:y].vegetation)






