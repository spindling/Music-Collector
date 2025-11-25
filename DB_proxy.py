# Proxy pattern used to limit database connection instantiation
import app_config

class DB_Interface:

    def __init__(self):
        pass

    def read_database(self):
        real_call = DB_Service()
        real_call.read_database()
    
class DB_Service:

    def __init__(self):
        self.cursor = None
        self.music_db = None

    def start_service(self):
        self.music_db = app_config.db_connection()
        self.music_db.setup()
        self.cursor = self.music_db.db_connection.cursor()
        self.clear_table()

    def clear_table(self):
        self.cursor.execute("DELETE from music_collection")

    def end_service(self):
        self.music_db.db_connection.close()
        self.cursor.close()

    def read_database(self):
        #example code
        cursor.execute("SELECT * FROM music_collection")
        results = cursor.fetchall()
        i = 1
        for result in results:
            print("Entry", i, result)
            i += 1

    def store_entry(self, entry):

        #self.cursor = self.music_db.db_connection.cursor()
        add_entry = "INSERT INTO music_collection (Title, Artist, format, TrackCount, Label, Date) VALUES (%s, %s, %s, %s, %s, %s)"
        
        data = (entry['Title'], entry['Artist'], entry['Format'], entry['Track-Count'], entry['Label'], entry['Date'])
        self.cursor.execute(add_entry, data)
        self.music_db.db_connection.commit() 
        #self.cursor.close()
        #music_db.db_connection.close()
        print("done")

class DB_Proxy:

    def __init__(self):
        pass

