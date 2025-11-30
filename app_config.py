# Set up database and API connections
import configparser
import mysql.connector
import musicbrainzngs as mbz

class db_connector:
    
    def __init__(self):
        self.db_login = None

    def setup(self):

        config = configparser.ConfigParser()
        config.read("config.cfg")
        
        self.db_login = mysql.connector.connect(
            host = config["MC_Database"]["host"],
            user = config["MC_Database"]["user"],
            password = config["MC_Database"]["password"],
            database = config["MC_Database"]["database"]
        )

class API_connector:

    def setup(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        
        mbz.set_useragent(config["MusicAPI"]["app_name"], 
                                          config["MusicAPI"]["version"], 
                                          config["MusicAPI"]["contact"])
        mbz.set_rate_limit(1,1)


