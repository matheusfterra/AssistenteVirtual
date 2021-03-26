from DBConnectors.DBHandler import *

#GET's
def get_values(logger):

    result = None
    try:
        mydb = DBHandler.get_mydb()
        cursor = mydb.cursor()
        cursor.execute('''
            SELECT * FROM TABLE WHERE NOT is_blocked
            ORDER BY last_login ASC
        ''')
        result = cursor.fetchall()

        users_list=[]
        user_credentials = {}
        if result:
            for r in result:
                # id
                user_credentials["id"] = r[0]
                # username
                user_credentials["username"] = r[1]
                #password
                user_credentials["password"] = r[2]

                users_list.append(user_credentials)

        cursor.close()
        mydb.close()
        return users_list

    except mysql.connector.Error as err:
        logger.error("Erro ao recuperar conta para login no banco de dados: ", err)

    try:
        cursor.close()
    except:
        logger.error("O cursor de execução do Banco de Dados já se encontra fechado!")
    try:
        mydb.close()
    except:
        logger.error("A conexão com o Banco de Dados já se encontra fechada!")





#INSERT's
def add_publications(logger,account_from_id,account_to_id,dir_media,localizacao,text,interations,is_video,original_link,origin_publicatedAt,aproved):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    try:
        cursor.execute("INSERT INTO publications(account_from_id,account_to_id,dir_media,location,text,interations,is_video,origin_publicatedAt,original_link,aproved) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(account_from_id,account_to_id,dir_media,localizacao,text,interations,is_video,origin_publicatedAt,original_link,aproved))
        mydb.commit()
        logger.info("Publicação cadastrada no Banco de Dados.")
    except mysql.connector.Error as err:
        logger.error(err)

    try:
        cursor.close()
    except:
        logger.error("O cursor de execução do Banco de Dados já se encontra fechado!")
    try:
        mydb.close()
    except:
        logger.error("A conexão com o Banco de Dados já se encontra fechada!")




#UPDATE's
def update_status_user_login(logger,id, status, time):
    try:
        mydb = DBHandler.get_mydb()
        cursor = mydb.cursor()
        cursor.execute("UPDATE account SET Status=%s, last_login = %s WHERE Id=%s",(status, time, id))
        mydb.commit()
    except mysql.connector.Error as err:
        logger.error("Erro ao fazer update de status de login de usuario no banco de dados: ", err)

    try:
        cursor.close()
    except:
        logger.error("O cursor de execução do Banco de Dados já se encontra fechado!")
    try:
        mydb.close()
    except:
        logger.error("A conexão com o Banco de Dados já se encontra fechada!")

