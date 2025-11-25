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
        print("Retrieving results...\n")
        metadata_retriever = API_facade.RetrieveMetadata_Facade(artist,album)
        results = metadata_retriever.find_metadata()
        return results
        
    def add_to_database(self, match):
        #Add database functionality
        db = DB_proxy.Database_Interface()
        db.read_database()

    def delete_from_database(self):
        pass


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def start(self):
        while True:
          user_input = self.view.menu()
          if user_input == "1":
              print("Debug: add entry")
              self.add_entry()
    
    def add_entry(self):
        artist,album = self.view.add_entry()
        print("Retrieving potential matches...")
        results = self.model.retrieve_results(artist,album)
        match = int(self.view.display_results(results))-1
        self.model.add_to_database(results[match])

    def modify_database(self):
        pass

    def retrieve_from_database(self):
        pass

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
        return input("Select: ")
    
    def add_entry(self):
        print("=================")
        print("Entry Creator")
        artist = input("Enter artist: ")   
        album = input("Enter release: ")
        return artist, album

    def display_results(self, results):
        for i in results:
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

    def delete_entry():
        pass

    def show_entries():
        pass

    def request_report():
        pass
