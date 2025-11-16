# Proxy pattern used for ensuring rate limiting when accessing API

class RetrieveMetadata:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def find_metadata():
        pass

class RetrieveMetadataProxy:

    def __init__(self, artist_name, album_name):
        self.artist_name = artist_name
        self.album_name = album_name

    def limit_rate():
        pass
    
    def find_metadata():
        pass

