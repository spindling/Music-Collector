# Model-View-Controller pattern for main interface 
import API_facade

class Model:
    
    def __init__(self):
        pass

    def create_report(self):
        pass

    def retrieve_report_data(self):
        pass

    def retrieve_results(self,artist,album):
        print("Retrieving results...")
        
        metadata_interface = API_facade.RetrieveMetadata_Interface(artist,album)
        results = metadata_interface.find_metadata()
        return results
        
    def add_to_database(self):
        pass

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
        self.view.display_results(results)
    
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

    def delete_entry():
        pass

    def show_entries():
        pass

    def request_report():
        pass
