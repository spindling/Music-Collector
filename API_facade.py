# API_facade.py
# - Connection to the API is simplified using the Facade pattern. 
# - Retrieve_Metadata_Facade is set up as the interface.
# - The find_metadata() method performs a sequence of actions
#   (using the QueryReleases class) that are required to 
#   submit queries to the API and format the result.
# - This allows for the retrieve_metadata() function within
#   the Model of mvc.py to use the Facade interface to
#   simplify interaction with the API.

import app_config

class RetrieveMetadata_Facade:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def find_metadata(self):
        query = QueryReleases(self.artist_name, self.album_name)
        query.setup_connection()
        query.submit_query()
        results = query.format_results()
        return results
    
class QueryReleases:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name
        self.__query_results = list

    def setup_connection(self):
        api = app_config.API_connector()
        api.setup()

    def submit_query(self):
        query = app_config.mbz.search_releases(artist=self.artist_name, release = self.album_name, limit = 3)
        self.__query_results = query

    def format_results(self):
        count = 0
        results = []
        for i in self.__query_results['release-list']:
            count += 1
            
            results.append({'Match #': count, 
                            'Artist': i['artist-credit-phrase'],
                            'Title': i['title'],
                            #'Format': i['medium-list'][0]['format'],
                            'Track-Count' : i['medium-list'][0]['track-count']
                            #'Label': i['label-info-list'][0]['label']['name']
                            })

            if 'label' in i['medium-list'][0]:
                results[-1]['Label'] = i['label-info-list'][0]['label']['name']
            else:
                results[-1]['Label'] = "n/a"
            if 'format' in i['medium-list'][0]:
                results[-1]['Format'] = i['medium-list'][0]['format']
            else:
                results[-1]['Format'] = "n/a"
            if 'date' in i:
                results[-1]['Date'] = i['date']
            else:
                results[-1]['Date'] = "n/a"
        return results
