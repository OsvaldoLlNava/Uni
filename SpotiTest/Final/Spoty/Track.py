class Track():

    def __init__(self,uri_track, name, artist, album, duration):
        self.uri_track = uri_track
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.uri_track != None:
            return  'El track es: {} \nArtista: {} \nAlbum: {}'.format(self.name,self.artist,self.album)
        else:
            return 'El track es: {} \nArtista: {} \nAlbum: {}'.format(self.name,self.artist,self.album)


    def __eq__(self, trackS):
        if trackS.uri_track != self.uri_track:
            return False

        if trackS.name != self.name:
            return False

        if trackS.artist != self.artist:
            return False

        if trackS.album != self.album:
            return False

        if trackS.duration != self.duration:
            return False
        return True
    
    def Get_ID(self):
        return self.uri_track
    
    def Get_Name(self):
        return self.name

    def Get_Artist(self):
        return self.artist

    def Get_Album(self):
        return self.album

    def Get_Duration(self):
        return self.duration
    
# id_track = '1234'
# name = 'waa'
# artist = 'chorizo'
# album = 'desayuno'
# duration = 'Todo el dia'
# cancion = Track(id_track,name,artist,album,duration)

# print(cancion)