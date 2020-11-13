import abc
from Piece import Piece

class Pawn(Piece):

    __pos = {"x": 0, "y": 0}

    @property
    def pos(self):
        return self.__pos

    def move(self, x, y):
        x_steps = abs(self.__pos["x"]-x)
        y_steps= abs(self.__pos["y"]-y)

        if y_steps > 0:
            return False
        if x_steps==2 and self.__pos["x"] ==6:
            return True
        elif x_steps==1:
            return True
            

