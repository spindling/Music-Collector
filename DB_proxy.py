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
        #self.clear_table()

    def clear_table(self):
        self.cursor.execute("DELETE from music_collection")

    def end_service(self):
        self.music_db.db_connection.close()
        self.cursor.close()

    def read_database(self):
        self.cursor.execute("SELECT * FROM music_collection")
        entries = self.cursor.fetchall()
   
        return entries

    def remove_entry(self, artist, album):
        del_entry = "DELETE FROM music_collection WHERE Artist = %s AND Title = %s"
        data = artist, album
        self.cursor.execute(del_entry, data)
        self.music_db.db_connection.commit()
        
    def store_entry(self, entry):

        add_entry = "INSERT INTO music_collection (Title, Artist, format, TrackCount, Label, Date) VALUES (%s, %s, %s, %s, %s, %s)"

        data = (entry['Title'], entry['Artist'], entry['Format'], entry['Track-Count'], entry['Label'], entry['Date'])
        self.cursor.execute(add_entry, data)
        self.music_db.db_connection.commit() 
     
        print("done")

class DB_Proxy:

    def __init__(self):
        pass

