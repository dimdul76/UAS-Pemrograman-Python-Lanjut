import mysql.connector, os, time

class Databases:
    def __init__(self,host,user,passwd,port,database,task=None):
        self.host = host
        self.user = user
        self.user = passwd
        self.port = port
        self.check_database = database
        self.task = task

        if self.task == "check":
            Databases.check_databases(host,user,passwd,port,database)
        else:
            return Databases.backup_databases(host,user,passwd,database)


    def check_databases(host, user, passwd, port, database):
        database = mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = passwd,
            database = database
        )

        return database.is_connected()
    
    def backup_databases(host, user, passwd, databases):
        DB_HOST = host
        DB_USER = user
        DB_USER_PASSWORD = passwd
        DB_NAME = databases
        date = time.strftime("%d-%m-%Y")
        try:
            os.stat(date)
        except:    
            os.mkdir(date)
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + f"./{date}/" +  DB_NAME + ".sql"
        os.system(dumpcmd)

    

# print(Databases.check_databases(host='192.168.99.248', user='root',passwd='2wsx1qaz',database="E-COMP",port=3306))
#Databases(host='localhost', user='root',passwd='2wsx1qaz',database="E-COMP",port=3306)

# date = time.strftime("%d-%m-%Y")
# print(date)