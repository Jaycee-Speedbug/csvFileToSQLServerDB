#!/usr/bin/python3 
#
#
#   
#   Programme Console traitant un fichier dont le path\filename sont passés en argument de la ligne de commande pour nourir une base de données
#
#   Le fichier doit être de type csv avec des ; pour délimiteurs
#   Le fichier doit contenir toutes les données permettant de créer un objet WildLifeMap
#   La carte portera le nom du fichier, duquel on a retiré l'extension .csv
#   Une fois validé, les champs de cet objet sont injectés dans la base de données SQL Server wildlife, avec
#   l'utilisateur wildlifeadmin
#
#   Les objets envisagés:
#   MapCell         Objet représentant une cellule de la carte de jeu
#   WildLifeMap     Objet contenant toutes les cellules d'une carte, ainsi que les données propres à la carte
#   SQLConnect      Objet chargé d'établir la connexion à la base de donnée et d'injecter les données d'une carte, ayant préalablement reçu
#                   un objet Map
#
#
#   Jaycee
#


from WildLife import *
import sys


def main():
    """Start point of csvFileToSQLServerDB"""
    print ("")
    print ("Arguments de la ligne de commande :")
    print ("")
    for argument in sys.argv:
        print(argument)


if __name__ == '__main__':
    main()

