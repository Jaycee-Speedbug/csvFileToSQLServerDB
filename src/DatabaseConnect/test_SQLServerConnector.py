#!/usr/bin/python3 
#
# Module regroupant les fonctions de tests unitaires de la classe:
#   SQLServerConnector
#
# Il peu y avoir des appels à des champs 'privés', pour les besoins des tests, quand les getters n'ont pas été codés
#


from SQLServerConnector import SQLServerConnector


def test():

    print("Tests on SQLServerConnector module")
    print("")

    print("SQL Server Version test")
    testConnector = SQLServerConnector('DESKTOP-AA2O89E', 'wildlife', 'wildlifeadmin', 'lulu1999')
    print(testConnector.checkServerVersion())





# Lance ce module de test
if __name__ == '__main__':
    test()
