#!/usr/bin/python3 
#
#   SQLServerConnector
#
#   Classe définissant un connecteur vers une base de données SQL Server
#
#
# More on the subject: https://stackoverflow.com/questions/3783238/python-database-connection-close
#
#


import pyodbc



class SQLServerConnector:
    """
    Connecteur vers une base de données SQL Server
    """

    @property
    def connex(self):
        return self._connex

    @connex.setter
    def connex(self, connexion):
        self._connex = connexion



    @property
    def curs(self):
        return self._curs

    @curs.setter
    def curs(self, cursor):
        self._curs = cursor



    # Chaine de connexion
    def connexionString(self, serverName, databaseName, userName, userPassword):
        str  = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + serverName
        str += ';DATABASE=' + databaseName
        str += ';UID=' + userName
        str += ';PWD=' + userPassword
        return str

        

    def __init__(self, serverName, databaseName, userName, userPassword):
        """
        Construction d'un objet de connexion à une base de données WildLife, sur un serveur SQL Server
        """

        if serverName == '':
            serverName = 'DESKTOP-AA2O89E'

        if databaseName == '':
            databasename = 'wildlife'

        if userName == '':
            userName = 'wildlifeadmin'
        
        if userPassword == '':
            userPassword = 'lulu1999'
        
        self.connex = pyodbc.connect(self.connexionString(serverName, databaseName, userName, userPassword))
        self.curs = self.connex.cursor()



    def checkServerVersion(self):
        #print("Checking SELECT @@version;")
        #print("")
        msg = ''
        self.curs.execute("SELECT @@version;") 
        row = self.curs.fetchone() 
        while row: 
            msg += row[0]
            row = self.curs.fetchone()
        return msg


        
        


