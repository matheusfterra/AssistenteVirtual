import mysql.connector
import DBConnectors.Constants as Constants

class DBHandler:
    def __init__(self):
        Constants.init()
        DBHandler.HOST = Constants.HOST
        DBHandler.USER = Constants.USER
        DBHandler.DBNAME = Constants.DATABASE
        DBHandler.PASSWORD = Constants.PASS
    
    @staticmethod
    def get_mydb():

        db = DBHandler()
        try:
            mydb = db.connect()
        except mysql.connector.Error as err:
            print("Erro ao conectar ao banco de dados: ", err)

        return mydb


    def connect(self):
        mydb = mysql.connector.connect(
            host=DBHandler.HOST,
            user=DBHandler.USER,
            passwd=DBHandler.PASSWORD,
            database = DBHandler.DBNAME
        )
        return mydb