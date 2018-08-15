#
# Fonction regroupant les tests des classes WildLifeMap et MapCell
#
# Il y a des appels à des champs 'privés' des classes de WildLifeMap pour les besoins des tests, quand les getters n'ont pas été codés
#



from WildLifeMap import WildLifeMap
from MapCell import MapCell
from wildlifeconst import *


def test():
    
    # Define a  map 3 x 3
    map = WildLifeMap("carte de test__XXX",3,3)

    # First row
    map.addCell(0,0,1,50,30)
    map.addCell(0,1,1,51,31)
    map.addCell(0,2,1,52,32)
    # Second row
    map.addCell(1,0,1,60,40)
    map.addCell(1,1,1,61,41)
    map.addCell(1,2,1,62,42)
    # Third row
    #map.addCell(2,0,1,71,50)    # One cell unaffected
    map.addCell(2,1,1,72,51)
    map.addCell(2,2,1,73,52)

    print("")
    print("Vegetation")
    for cell in map._cells:
        print(cell.vegetation())



    ################################################   TESTS   ################################################

    # Test 1 - Try to read a Cell
    testCell = map.getCellAt(0,0)
    if map.getCellAt(0,0).vegetation() == 30:
        print("TEST 1 OK")
    else:
        print("TEST 1 FAIL")

    # Test 2 - Try to 'add' a cell outside the Map
    if map.addCell(0,3,1,1,1):
        print("TEST 2 FAIL")
    else:
        print("TEST 2 OK")

    # Test 3 - Try to read an unaffected Cell
    if map.getCellAt(2,0) is type(MapCell):
        print("TEST 3 FAIL")
    else:
        print("TEST 3 OK")

    # Test 4 - Map name should be a 15 chars len string
    if len(map.name()) > MAP_NAME_MAX_LEN:
        print("TEST 4 FAIL")
    else:
        print("TEST 4 OK")

    # Test 5 - Map width test
    if map._width == 3:
        print("TEST 5 OK")
    else:
        print("TEST 5 FAIL")

    # Test 6 - Map height test
    if map._height == 3:
        print("TEST 6 OK")
    else:
        print("TEST 6 FAIL")

    # Test 7 - Map width test
    if map.mapSize() == 9:
        print("TEST 7 OK")
    else:
        print("TEST 7 FAIL")








# Lance ce module de test
if __name__ == '__main__':
    test()

