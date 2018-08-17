#!/usr/bin/python3 
#
#   SQLServerConnector
#
#   Classe définissant un connecteur vers une base de données SQL Server
#

import pyodbc



class SQLServerConnector(object):
    """
    Connecteur vers une base de données SQL Server
    """



    @property
    def connex(self):
        """getter"""
        return self._connex



    @property
    def cursor(self):
        """getter"""
        return self._cursor



    # Nom du server
    def _get_serverName(self):
        """getter"""
        return self._serverName

    def _set_serverName(self, name):
        """setter"""
        self._serverName = name

    server = property(_get_serverName, _set_serverName)



    # Nom de la base de données
    def _get_databaseName(self):
        """getter"""
        return self._databaseName

    def _set_databaseName(self, name):
        """setter"""
        self._databaseName = name

    database = property(_get_databaseName, _set_databaseName)



    # Nom de la connexion SQL Server
    def _get_userName(self):
        """getter"""
        return self._userName

    def _set_userName(self, name):
        """setter"""
        self._userName = name

    user = property(_get_userName, _set_userName)



    # Password
    @property
    def password(self):
        """getter"""
        return self._password



    def newConnexion(self, serverName, databaseName, userName, userPassword):

        if len(serverName) > 0:
            server = serverName

        if len(databaseName) > 0:
            database = databaseName

        if len(userName) > 0:
            user = userName

        if len(userPassword) > 0:
            password = userPassword

        self._connex = pyodbc.connect(connexionString)
        self._cursor = connex.cursor()



    @property
    def connexionString(self):
        str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + serverName
        str+= ';DATABASE=' + databaseName
        str+= ';UID=' + userName
        str+= ';PWD=' + password
        return str



    def __init__(self):
        """
        Construction d'un objet de connexion à une base de données WildLife, sur un serveur SQL Server
        """

        # Informations de connexion
        serverName = 'DESKTOP-AA2O89E' 
        databaseName = 'wildlife' 
        userName = 'wildlifeadmin' 
        password = 'lulu1999'

        connex = pyodbc.connect(connexionString)
        cursor = connex.cursor()

        newConnexion("", "", "", "")



    def checkDatabase(self):
        
        pass

        
        


