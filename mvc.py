# Model-View-Controller pattern for main interface 
import API_facade
import DB_proxy

class Model:
    
    def retrieve_metadata(self,artist,album):
        metadata_retriever = API_facade.RetrieveMetadata_Facade(artist,album)
        results = metadata_retriever.find_metadata()
        return results
    
    def add_to_database(self, match):
        db = DB_proxy.DB_Proxy()
        db.store_entry(match)
    
    def delete_db_entry(self, artist, album):
        db = DB_proxy.DB_Proxy()
        db.remove_entry(artist,album)

    def clear_db(self):
        db = DB_proxy.DB_Proxy()
        db.clear_table()

    def retrieve_all_entries(self):
        db = DB_proxy.DB_Proxy()
        all_entries = db.read_database()
        return all_entries
        

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def start(self):
        while True:
            user_input = self.view.menu()
            if user_input == "1":
                self.add_entry()
            elif user_input == "2":
                self.delete_entry()
            elif user_input == "3":
                self.retrieve_report_data()
            elif user_input == "4":
                self.delete_all_entries()
            elif user_input == "5":
                quit()

    def add_entry(self):
        artist,album = self.view.add_entry()
        results = self.model.retrieve_metadata(artist,album)
        match = int(self.view.display_results(results))-1
        self.model.add_to_database(results[match])

    def delete_entry(self):
        artist, album = self.view.delete_entry()
        self.model.delete_db_entry(artist,album)

    def delete_all_entries(self):
        choice = self.view.delete_database()
        if choice == "y" or choice == "Y":
            self.model.clear_db()

    def retrieve_report_data(self):
        all_entries = self.model.retrieve_all_entries()
        choice = self.view.generate_report(all_entries)
        return choice
        

class View:

    def menu(self):
        print("")
        print("=================")
        print("Music Collector")
        print("-----------------")
        print("Main Menu")
        print("1. Add entry")
        print("2. Delete entry")
        print("3. Generate Report")
        print("4. Clear database")
        print("5. Exit program")
        return input("Enter option #: ")
    
    def add_entry(self):
        print("")
        print("=================")
        print("Add Entry")
        print("-----------------")
        artist = input("Enter artist: ")   
        album = input("Enter release: ")
        return artist, album

    def display_results(self, results):
        print("")
        print("=================")
        print("Matching Results")
        print("-----------------")
        for i in results:
            print("")
            print("Match #: ",i['Match #'])
            print("Title: ", i['Title'])
            print("Artist: ", i['Artist'])
            if 'Date' in i:
                print("Release date: ", i['Date'])
            print("Format: ", i['Format'])
            print("Track Count: ", i['Track-Count'])
            print("Label: ", i['Label'])
        return input("Choose matching result #: ")

    def delete_entry(self):
        print("")
        print("=================")
        print("Delete Entry")
        print("-----------------")
        artist = input("Enter artist: ")
        album = input("Enter release: ")
        return artist,album

    def generate_report(self, entries):
        print("")
        print("=================")
        print("Your Collection")
        print("-----------------")
        for i, data in enumerate(entries):
            print("")
            print("Entry #", i+1)
            print("Title: ", data[0])
            print("Artist: ", data[1])
            print("Format: ", data[2])
            print("Track Count: ", data[3])
            print("Label: ", data[4])
            print("Date :", data[5])
        
    def delete_database(self):
        return input("DELETE ALL ENTRIES\nAre you sure? (y/n): ")
