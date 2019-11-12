from abc import ABC, abstractmethod

class DBService(ABC):
    @abstractmethod
    def saveTrack(self, track):
        pass

    @abstractmethod
    def DeleteTrack(self, nombre, artista):
        pass

    @abstractmethod
    def showTracks(self):
        pass