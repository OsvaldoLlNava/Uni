# import Syncro
import Syncro
import LeerCredenciales
import Track

if __name__ == '__main__':
    credenciales = LeerCredenciales.Leer_Credenciales('Credenciales.txt')
    # # print(credenciales)
    # username ='31hzoj7ckzb2dgudlq5zfbudzoia'
    # clientId='005e25714bad49ab93e394adeabaaa96'
    # clientSecret='087a97142beb44a18e818424ae2b444c'
    syn = Syncro.syncro(credenciales[0], credenciales[1], credenciales[2])

    # syn.Search_Track('smells', 'nirvana')
    # tomate = syn.Get_Track('Smells Like Teen Spirit', 'Nirvana', 'Nevermind (Super Deluxe Edition)')

    syn.Show_Tracks()
    # syn.Delete_Track(tomate)
    # syn.Add_Track(tomate)
    # res = Track('123','vacio','vacio', 'vacio','vacio')
    # print(res)

    # sp = Spoty.Spoty(username, clientId, clientSecret)
    # sp.Search_Track('country roads', 'john', 'Poems')