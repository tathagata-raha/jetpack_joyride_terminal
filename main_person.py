from config import Config
class Main_person():
    def __init__(self,xcoo,ycoo,height,width,board):
        self._xcoo=xcoo
        self._ycoo=ycoo
        self._height=height
        self._width=width
        self._grid=board.get_grid()
        self._lives=5
    
    def disappeaar_person(self):
        for i in range(self._ycoo,self._ycoo+self._height):
            for j in range(self._xcoo,self._xcoo+self._width):
                self._grid[i][j]=Config.disappear_mario

    def get_xcoo(self):
        return self._xcoo

    def get_ycoo(self):
        return self._ycoo

    def get_lives(self):
        return self._lives

    def lose_life(self):
        self._lives-=1