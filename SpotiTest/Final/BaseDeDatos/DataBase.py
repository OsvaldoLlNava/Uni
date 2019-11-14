import sqlite3
import DBAbs
from Spoty import Track

class DataBase(DBAbs.DBService):
    def Crear_Tabla ():
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

    def Drop_Table(nombre):
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
    def Agregar_Cancion(Id_Cancion, Nombre_Cancion, Artista_Cancion, Album_Cancion, Duracion_Cancion):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO canciones VALUES 
                    ('{}', '{}', '{}', '{}', '{}')""".format(Id_Cancion, Nombre_Cancion, Artista_Cancion ,Album_Cancion, Duracion_Cancion)
            resultado = cursor.execute(query)
            conexion.commit()
            print('Valor Insertado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


    """ ID Text,
                        Name Text,
                        Artist Text,
                        Album Text,
                        Duration Text"""
    #Select

    def Ver_Todo():
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

    def Ver_Uno(id_elemento):
        try:
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

    def Eliminar_Elemento(Id_Elemento):
        try:
            conexion = sqlite3.connect('Spotipy.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = "DELETE FROM Canciones WHERE id = {}".format(Id_Elemento)
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
