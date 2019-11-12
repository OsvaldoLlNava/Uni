from abc import ABC, abstractmethod

class SFYSERVICE(ABC):
    @abstractmethod
    def buscarNombre(self, trackName, artist):
        pass

    @abstractmethod
    def agregarCancion(self, trackName, artist):
        pass

    @abstractmethod
    def borrarCancion(self, trackName, artist):
        pass

    @abstractmethod
    def mostrarCanciones(self):
        pass
