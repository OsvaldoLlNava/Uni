import sqlite3
from DBAbs import DBService
from Spoty import Track

class DataBase(DBService):
    def Crear_Tabla (self):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = '''CREATE TABLE IF NOT EXISTS canciones (
                        ID Text,
                        Name Text,
                        Artist Text,
                        Album Text,
                        Duration Text
                    );'''

            cursor.execute(query)
            conexion.commit()
            print('Tabla creada con éxito')
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexión!', error)
        finally:
            if (conexion):
                conexion.close()
                print('Conexión a SQLite cerrada\n')

    def Drop_Table(self, nombre):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = '''DROP TABLE {}; '''.format(nombre)

            cursor.execute(query)
            conexion.commit()
            print('Tabla Eliminada con éxito')
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexión!', error)
        finally:
            if (conexion):
                conexion.close()
                print('Conexión a SQLite cerrada\n')


        #Insert
    def saveTrack(self, Track):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO canciones VALUES 
                    ('{}', '{}', '{}', '{}', '{}')""".format(Track.uri_track, Track.name, Track.artist , Track.album, Track.duration)
            resultado = cursor.execute(query)
            conexion.commit()
            print('Valor Insertado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


    #Select

    def showTracks(self):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM canciones;'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print('Id: {}\nNombre de la Cancion: {}\nArtista: {}\nAlbum: {}\nDuracion: {}'.format(*row))
            
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


    #Select Simgular

    def Ver_Uno(self, Track):
        try:
            #ID_elemento
            id_elemento = Track.uri_track
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM canciones where Id = {};'.format(id_elemento)
            cursor.execute(query)
            rows = cursor.fetchall()

            print('----------Registro id = {}-------------'.format(id_elemento))

            for row in rows:
                print('Id: {}\nNombre de la Cancion: {}\nArtista: {}\nAlbum: {}\nDuracion: {}'.format(*row))
            
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


    #Delete

    def DeleteTrack(self, Track):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = "DELETE FROM Canciones WHERE id = {}".format(Track.uri_track)
            resultado = cursor.execute(query)
            conexion.commit()
            print('Valor Eliminado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


    #Update

    # def Actualizar_Elemento(id_elemento, espacio, nuevo_valor):
    #     try:
    #         conexion = sqlite3.connect('mi_base_de_datos.db')
    #         cursor = conexion.cursor()
    #         print('Conectado')

    #         query = """UPDATE CA SET {} = '{}' where Id = {}""".format(espacio, nuevo_valor, id_elemento)
    #         resultado = cursor.execute(query)
    #         conexion.commit()
    #         print('Valor Actualizado Correctamente', resultado)
    #         cursor.close()

    #     except sqlite3.Error as error:
    #         print('Error con la conexion',error)

    #     finally:
    #         if(conexion):
    #             conexion.close()