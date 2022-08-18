import os
from config import Config
class Board:
    # Map of the game
    def __init__(self, height, width):
        self._height=height
        self._width=width
        self.grid=[]
        for i in range (self._height): #rows                              
            self.new = []                 
            for j in range (self._width): #columns  
                self.new.append(" ")
            self.grid.append(self.new)
    
    def get_width(self):
        return self._width

    def get_grid(self):
        return self.grid
    def get_height(self):
        return self._height

    def get_char(self,ycoo,xcoo):
        return self.grid[ycoo][xcoo]

    def del_char_from_map(self,ycoo,xcoo):
        self.grid[ycoo][xcoo]=' '+'\033[0m'

    def print_it(self,start_co,score,lives,shield_status,dlives):
        print("Score: " + str(score) +"\tLives: "+str(lives) + "\tBoss lives: "+str(dlives),end="\t")
        if(shield_status==0):
            print(Config.shield_not_ready)
        elif(shield_status==1):
            print(Config.shield_ready)
        elif(shield_status==2):
            print(''+'\033[0m'+Config.shield_on)
        elif(shield_status==4):
            print(''+'\033[0m'+Config.shield_disabled)
        tempstr=""
        for i in range(self._height):
            for j in range(start_co,start_co+170):
                tempstr+=(self.grid[i][j])
            tempstr+='\n'
        print(tempstr)

