#
# Simple test of the classes WildLifeMap and MapCell
#
#



from WildLifeMap import WildLifeMap
from MapCell import MapCell
from wildlifeconst import *


def test():
    
    # Define a  map 3 x 3
    map = WildLifeMap("carte de test__XXX",3,3)

    print("Nom de la carte créée: " + map._name)
    print("Width: " + str(map._width))
    print("Height: " + str(map._height))
    print("Size: " + str(map.mapSize()))
    print("")

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


    # Test 1 - Try to read a Cell
    testCell = map.getCellAt(0,0)
    if map.getCellAt(0,0)._vegetation == 30:
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
    if len(map._name) > MAP_NAME_MAX_LEN:
        print("TEST 4 FAIL")
    else:
        print("TEST 4 OK")

    print("")
    print("Vegetation")
    for cell in map._cells:
        print(cell._vegetation)






# Lance ce module de test
if __name__ == '__main__':
    test()

