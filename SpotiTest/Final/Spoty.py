import spotipy
import spotipy.util as util
import pprint
# from Track import Track
from Track import Track
from SPYAbs import SFYSERVICE

class Spoty(SFYSERVICE):
    def __init__(self, user_name, Client_id, Client_Secret):
        username = user_name
        scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
        clientId= Client_id
        clientSecret= Client_Secret
        self.token = util.prompt_for_user_token(username,scope=scopes,client_id=clientId,client_secret=clientSecret,redirect_uri='http://google.com/')
        self.sp = spotipy.Spotify(auth=self.token)

    def Get_Track(self, nombre, artista, album):
        if self.token:
            self.sp.trace = False
            results = self.sp.search(q='artist:' + artista + ' track:' +nombre + ' album:' + album)
            for track in results['tracks']['items']:
                id_track = track['id']
                name = track['name']
                artist = track['artists'][0]['name']
                album = track['album']['name']
                duration = track['duration_ms']
            objectTrack = Track(id_track,name,artist,album,duration)
            return objectTrack
        else:
            print("Can't get token for", self.token)
    
    def Search_Track(self, nombre, artista):
        if self.token:
            self.sp.trace = False
            results = self.sp.search(q= 'artist:' + artista + ' track:' +nombre, limit = 15)
            for track in results['tracks']['items']:
                print()
                print('ID = {}\nName = {}\nArtist = {}\nAlbum = {}'.format(track['id'], track['name'], track['artists'][0]['name'], track['album']['name']))
                print('\n----------------------------------------------------------------')
        else:
            print("Can't get token for", self.token)


    def Get_Track_Id(self,nombre,artista):
        if self.token:
            self.sp.trace = False
            results = self.sp.search(q='artist:' + artista + ' track:' + nombre,limit=2)
            for track in results['tracks']['items']:
                print(track['name'] + ' - ' + track['artists'][0]['name'])

            return track['id']
        else:
            print("Can't get token for", self.token)

    # def Add_Tracks(self, lista_tracks):
    #     if self.token:
    #         self.sp.trace = False
    #         self.sp.current_user_saved_tracks_add(lista_tracks)
    #         print('Las canciones \n {} \nFueron agregadas'.format(lista_tracks))
    #     else:
    #         print("Can't get token for", self.token)
    
    def Add_Track(self, Track):
        if self.token:
            self.sp.trace = False
            lista_tracks =[Track.uri_track]
            self.sp.current_user_saved_tracks_add(lista_tracks)
            print('La cancion \n Nombre: {} \nArtista: {}\nFue agregada'.format(Track.name, Track.artist))
        else:
            print("Can't get token for", self.token)

    # def Delete_Track(self, lista_tracks):
    #     if self.token:
    #         self.sp.trace= False
    #         self.sp.current_user_saved_tracks_delete(lista_tracks)
    #         print('Las canciones \n {} \nFueron eliminadas'.format(lista_tracks))
    #     else:
    #         print("Can't get token for", self.token)

    def Delete_Track(self, Track):
        if self.token:
            self.sp.tarce = False
            lista_tracks =[Track.uri_track]
            self.sp.current_user_saved_tracks_delete(lista_tracks)
            print('La cancion \nNombre: {} \nArtista: {}\nFue eliminada'.format(Track.name, Track.artist))
    
    def Show_Tracks(self):
        if self.token:
            self.sp.trace = False
            results = self.sp.current_user_saved_tracks()
            print('-------------------------')
            for item in results['items']:
                track = item['track']
                print('Nombre: {}\nArtista: {}\nAlbum: {}'.format(track['name'],track['artists'][0]['name'],track['album']['name']))
                print('-------------------------')
        else:
            print("Can't get token for", self.token)

if __name__ == '__main__':
    username = '31hzoj7ckzb2dgudlq5zfbudzoia'
    clientId='005e25714bad49ab93e394adeabaaa96'
    clientSecret='087a97142beb44a18e818424ae2b444c'

    spotify = Spoty(username, clientId, clientSecret)

    # spotify.Search_Track('country roads', 'john', 'Poems')
    spotify.Search_Track('acerca','ambkor')

    
    res = spotify.Get_Track('acerca','ambkor','aullidos')
    print(res)
    # spotify.Delete_Track(res)
    # spotify.Add_Track(res)
    # cancion = spotify.Get_Track('country roads', 'john', 'Poems')
    # print(cancion)
    # spotify.Show_Tracks()
    # a = 'khan doblel'
    # n = 'rain'

    # spotify.Add_Tracks_With_Specific_Names(n,a)