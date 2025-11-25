#Facade pattern used to simplify API access
import app_config

class RetrieveMetadata_Facade:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def find_metadata(self):
        query = QueryReleases(self.artist_name, self.album_name)
        query.submit_query()
        results = query.format_results()
        return results

class QueryReleases:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name
        self.query_results = None

    def submit_query(self):
        api = app_config.API_connection()
        api.setup()
        query = app_config.mbz.search_releases(artist=self.artist_name, release = self.album_name, limit = 2)
        self.query_results = query
        #return query
    
    def format_results(self):
        count = 0
        results = []
        for i in self.query_results['release-list']:
            count += 1
            
            results.append({'Match #': count, 
                            'Artist': i['artist-credit-phrase'],
                            'Title': i['title'],})
            
            results[-1]['Format'] = i['medium-list'][0]['format']
            results[-1]['Track-Count'] = i['medium-list'][0]['track-count']
            results[-1]['Label'] = i['label-info-list'][0]['label']['name']
            if 'date' in i:
                results[-1]['Date'] = i['date']
        return results
    
    def select_match():
        pass

class FormatEntry:
    
    def format_metadata():
        pass

#artist = "Green Day"
#album = "American Idiot"
#interface = RetrieveMetadata_Interface(artist, album)
#interface.find_metadata()