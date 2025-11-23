# Model-View-Controller pattern for main interface 

class Model:
    
    def __init__(self):
        pass

    def create_report():
        pass

    def retrieve_report_data():
        pass

    def retrieve_metadata():
        pass

    def add_to_database():
        pass

    def delete_from_database():
        pass


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def start(self):
        self.view.menu()

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
        print("Select from menu")
        print("1. Add entry")

    
    def add_entry():
        pass

    def delete_entry():
        pass

    def show_entries():
        pass

    def request_report():
        pass
