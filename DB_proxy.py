# Proxy pattern used to provide logging functionality
import app_config
from abc import ABC

class DB_Interface(ABC):

    def start_service(self):
        pass

    def clear_table(self):
        pass
 
    def end_service(self):
        pass

    def read_database(self):
        print("Hell yeah!")

    def remove_entry(self, artist, album):
        pass

    def store_entry(self, entry):
        pass
    
class DB_Service(DB_Interface):

    def __init__(self):
        self.cursor = None
        self.music_db = None
 
  
    def start_service(self):
        self.music_db = app_config.db_connector()
        self.music_db.setup()
        self.cursor = self.music_db.db_login.cursor()

    def clear_table(self):
        self.start_service()
        self.cursor.execute("DELETE from music_collection")
        self.end_service()
 
    def end_service(self):
        self.music_db.db_login.close()
        self.cursor.close()

    def read_database(self):
        self.start_service()
        self.cursor.execute("SELECT * FROM music_collection")
        entries = self.cursor.fetchall()
        self.end_service()
        return entries

    def remove_entry(self, artist, album):
        self.start_service()
        del_entry = "DELETE FROM music_collection WHERE Artist = %s AND Title = %s"
        data = artist, album
        self.cursor.execute(del_entry, data)
        self.music_db.db_login.commit()
        self.end_service()

    def store_entry(self, entry):
        self.start_service()
        add_entry = "INSERT INTO music_collection (Title, Artist, format, TrackCount, Label, Date) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (entry['Title'], entry['Artist'], entry['Format'], entry['Track-Count'], entry['Label'], entry['Date'])
        self.cursor.execute(add_entry, data)
        self.music_db.db_login.commit() 
        self.end_service()

        
 
class DB_Proxy(DB_Interface):
    ## Proxy functions as a logger for Database functions
    def __init__(self):
        self.service = DB_Service()

    def start_service(self):
        self.service.start_service

    def clear_table(self):
        print("")
        print("Deleting all entries...")
        self.service.clear_table
 
    def end_service(self):
        self.service.end_service()

    def read_database(self):
        print("")
        print("Retrieving entries...")
        results = self.service.read_database()
        print("")
        return results

    def remove_entry(self, artist, album):
        print("")
        print("Removing entry...")
        self.service.remove_entry(artist,album)
        print("Entry removed!")
        print("")

    def store_entry(self, entry):
        print("")
        print("Storing entry...")
        self.service.store_entry(entry)
        print("Entry stored in database!")
        print("")

