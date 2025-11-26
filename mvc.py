# Model-View-Controller pattern for main interface 
import API_facade
import DB_proxy

class Model:
    
    def __init__(self):
        pass

    def create_report(self):
        pass

    def retrieve_report_data(self):
        pass

    def retrieve_results(self,artist,album):
        metadata_retriever = API_facade.RetrieveMetadata_Facade(artist,album)
        results = metadata_retriever.find_metadata()
        return results
        
    def add_to_database(self, match):
        #Add database functionality
        db = DB_proxy.DB_Service()
        db.start_service()
        db.store_entry(match)
        db.end_service()

    def delete_db_entry(self, artist, album):
        db = DB_proxy.DB_Service()
        db.start_service()
        db.remove_entry(artist,album)
        db.end_service()

    def clear_db(self):
        db = DB_proxy.DB_Service()
        db.start_service()
        db.clear_table()
        db.end_service()

    def retrieve_all_entries(self):
        db = DB_proxy.DB_Service()
        db.start_service()
        all_entries = db.read_database()
        db.end_service()
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
                self.retrieve_from_database()
            elif user_input == "4":
                self.delete_all_entries()

    def add_entry(self):
        artist,album = self.view.add_entry()
        results = self.model.retrieve_results(artist,album)
        match = int(self.view.display_results(results))-1
        self.model.add_to_database(results[match])

    def delete_entry(self):
        artist, album = self.view.delete_entry()
        self.model.delete_db_entry(artist,album)

    def delete_all_entries(self):
        choice = self.view.confirm_choice()
        if choice == "y":
            self.model.clear_db()

    def modify_database(self):
        pass

    def retrieve_from_database(self):
        all_entries = self.model.retrieve_all_entries()
        choice = self.view.show_entries(all_entries)
        return choice

    def generate_report(self):
        pass


class View:

    def __init__(self):
        pass
    
    def menu(self):
        print("=================")
        print("Music-Collector")
        print("")
        print("Main Menu")
        print("1. Add entry")
        print("2. Delete entry")
        print("3. Display existing entries")
        print("4. Delete all entries")
        return input("Enter option #: ")
    
    def add_entry(self):
        print("=================")
        print("Add Entry")
        artist = input("Enter artist: ")   
        album = input("Enter release: ")
        return artist, album

    def display_results(self, results):
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
            print("")
        return input("Enter matching result #: ")

    def delete_entry(self):
        print("=================")
        print("Delete Entry")
        artist = input("Enter artist: ")
        album = input("Enter release: ")
        return artist,album

    def show_entries(self, entries):
        print("\nDisplaying entries: ")
        for i, data in enumerate(entries):
            print("")
            print("Entry #", i+1)
            print("Title: ", data[0])
            print("Artist: ", data[1])
            print("Format: ", data[2])
            print("Track Count: ", data[3])
            print("Label: ", data[4])
            print("Date :", data[5])
            print("")


    def confirm_choice(self):
        return input("Are you sure? (y/n)")

    def request_report():
        pass
