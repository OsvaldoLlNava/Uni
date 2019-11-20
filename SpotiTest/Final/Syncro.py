from BaseDeDatos.DataBase import DataBase
from Spoty.Spoty import Spoty
from Spoty.Track import Track

class syncro ():

    def __init__(self, user_name, Client_id, Client_Secret):
        self.username = user_name
        self.scopes= 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read '
        self.clientId= Client_id
        self.clientSecret= Client_Secret
        self.sp = Spoty(self.username, self.clientId, self.clientSecret)
        self.bd = DataBase()
        self.bd.Crear_Tabla()


    def Add_Track(self, Track):
        self.sp.Add_Track(Track)
        self.bd.saveTrack(Track)
    
    def Delete_Track(self, Track):
        self.sp.Delete_Track(Track)
        self.bd.DeleteTrack(Track)
    
    def Show_Tracks(self, opcion):
        if opcion == 1:
            self.sp.Show_Tracks()
        elif opcion == 2:
            self.bd.showTracks()
        else:
            return 0

    def Search_Track(self, nombre, artista, album=''):
        self.sp.Search_Track(nombre, artista, album)
        

    

    

username = '31hzoj7ckzb2dgudlq5zfbudzoia'
clientId='005e25714bad49ab93e394adeabaaa96'
clientSecret='087a97142beb44a18e818424ae2b444c'
