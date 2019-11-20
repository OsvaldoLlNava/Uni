from abc import ABC, abstractmethod

class SFYSERVICE(ABC):
    @abstractmethod
    def Get_Track(self, trackName, artist):
        pass

    @abstractmethod
    def Add_Track(self):
        pass

    @abstractmethod
    def Delete_Track(self):
        pass

    @abstractmethod
    def Show_Tracks(self):
        pass
