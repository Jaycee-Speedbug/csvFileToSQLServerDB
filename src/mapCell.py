#
#   MapCell
#
#   Classe définissant une carte de jeu WildLife
#


class MapCell:
    """Documentation"""

    coordX = -1
    coordY = -1
    humidite = -1
    vegetation = -1



    def __init__(self,x,y,hum,veg):
        """Initialisation d'une cellule de carte"""
        coordX = x
        coordY = y
        humidity = hum
        vegetation = veg


