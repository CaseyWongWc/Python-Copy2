class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        if new_side <= 0:
            raise ValueError("Side length must be positive")
        else:
            self.__side = new_side
