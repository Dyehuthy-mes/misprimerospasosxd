import abc

class Piece(metaclass=abc.ABCMeta):
    
    @property
    @abc.abstractmethod
    def pos(self):
        return

    @pos.setter
    @abc.abstractmethod
    def pos(self, x, y):
        self.__pos = {"x": x, "y": y}