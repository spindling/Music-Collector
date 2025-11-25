# Proxy pattern used for ensuring rate limiting when accessing API
import app_config

class Database_Interface:

    def __init__(self):
        pass

    def read_database(self):
        real_call = DB_Service()
        real_call.read_database()

    
class DB_Service:

    def __init__(self):
        pass   

    def read_database(self):
        music_db = app_config.db_connection()
        music_db.setup()
        #Perhaps make this neater
        cursor = music_db.db_connection.cursor()
    
        #example code
        cursor.execute("SELECT * FROM music_collection")
        results = cursor.fetchall()
        i = 1
        for result in results:
            print("Entry", i, result)
            i += 1

class DB_Proxy:

    def __init__(self):
        pass

call_db = DB_Service()
call_db.read_database()
