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

    def delete_from_database(self):
        pass

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
          if user_input == "2":
                self.retrieve_from_database()
              
    
    def add_entry(self):
        artist,album = self.view.add_entry()
        results = self.model.retrieve_results(artist,album)
        match = int(self.view.display_results(results))-1
        self.model.add_to_database(results[match])

    def modify_database(self):
        pass

    def retrieve_from_database(self):
        all_entries = self.model.retrieve_all_entries()
        self.view.show_entries(all_entries)

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
        print("2. Display entries")
        return input("Select: ")
    
    def add_entry(self):
        print("=================")
        print("Entry Creator")
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

    def delete_entry():
        pass

    def show_entries(self, entries):
        for i in entries:
            print("")
            print("Title: ", i[0])
            print("Artist: ", i[1])
            print("Format: ", i[2])
            print("Track Count: ", i[3])
            print("Label: ", i[4])
            print("Date :", i[5])
            print("")
        #print(entries)

    def request_report():
        pass
