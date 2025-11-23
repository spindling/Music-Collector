# Set up database and API connections
import configparser
import mysql.connector
import musicbrainzngs as mbz

class db_connection:
    
    def __init__(self):
        self.db_conn = None

    def setup(self):

        config = configparser.ConfigParser()
        config.read("config.cfg")
        
        self.db_conn = mysql.connector.connect(
            host = config["MC_Database"]["host"],
            user = config["MC_Database"]["user"],
            password = config["MC_Database"]["password"],
            database = config["MC_Database"]["database"]
        )


class API_connection:

    def __init__(self):
        self.api_conn = None

    def setup(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")

        self.api_conn = mbz.set_useragent(config["MusicAPI"]["app_name"], 
                                          config["MusicAPI"]["version"], 
                                          config["MusicAPI"]["contact"])
        mbz.set_rate_limit(1,1)
        #query = mbz.search_releases("Green Day", "American Idiot", 1)
        #print(query)
        #print(self.api_conn)

#
#api = API_connection()
#api.setup()
#print(api)



