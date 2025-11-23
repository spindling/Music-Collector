# Facade pattern used to simplify API access
import app_config

class RetrieveMetadata_Interface:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def find_metadata(self):
        releases = QueryReleases(self.artist_name, self.album_name)
        releases.search_releases()

class QueryReleases:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def search_releases(self):
        api = app_config.API_connection()
        api.setup()
        query = app_config.mbz.search_releases(artist=self.artist_name, release = self.album_name, limit = 2)
        
        #print(query)
        count = 0
        for i in query['release-list']:
            count += 1
            print("Match #",count)
            print(i['title'])
            print("")

        

    def select_match():
        pass

class FormatEntry:
    
    def format_metadata():
        pass

artist = "Green Day"
album = "American Idiot"
interface = RetrieveMetadata_Interface(artist, album)
interface.find_metadata()