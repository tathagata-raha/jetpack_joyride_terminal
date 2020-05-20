from main_person import Main_person
from config import Config
class Dragon(Main_person):
    def __init__(self,xcoo,ycoo,board,scene):
        Main_person.__init__(self,xcoo,ycoo,4,4,board)
        self._scene=scene
        self._prevtime=0
        self._skiptime=0.5
        self._lives=20

    def place_on_map(self):
        self._grid[self._ycoo][self._xcoo]=Config.dragon+'^'+'\033[0m'
        self._grid[self._ycoo][self._xcoo+1]=Config.dragon+'-'+'\033[0m'
        self._grid[self._ycoo][self._xcoo+2]=Config.dragon+'-'+'\033[0m'
        self._grid[self._ycoo][self._xcoo+3]=Config.dragon+'^'+'\033[0m'
        self._grid[self._ycoo+1][self._xcoo]=Config.dragon+'m'+'\033[0m'
        self._grid[self._ycoo+1][self._xcoo+1]=Config.dragon+' '+'\033[0m'
        self._grid[self._ycoo+1][self._xcoo+2]=Config.dragon+' '+'\033[0m'
        self._grid[self._ycoo+1][self._xcoo+3]=Config.dragon+'m'+'\033[0m'
        self._grid[self._ycoo+2][self._xcoo]=Config.dragon+'('+'\033[0m'
        self._grid[self._ycoo+2][self._xcoo+1]=Config.dragon+'^'+'\033[0m'
        self._grid[self._ycoo+2][self._xcoo+2]=Config.dragon+'^'+'\033[0m'
        self._grid[self._ycoo+2][self._xcoo+3]=Config.dragon+')'+'\033[0m'
        self._grid[self._ycoo+3][self._xcoo]=Config.dragon+'v'+'\033[0m'
        self._grid[self._ycoo+3][self._xcoo+1]=Config.dragon+'-'+'\033[0m'
        self._grid[self._ycoo+3][self._xcoo+2]=Config.dragon+'-'+'\033[0m'
        self._grid[self._ycoo+3][self._xcoo+3]=Config.dragon+'v'+'\033[0m'

    def checkupcollision(self):
        if(self._ycoo==3):
            return 0
        else:
            return 1

    def checkdowncollision(self):
        if(self._ycoo==33):
            return 0
        else:
            return 1

    def jump(self,manda):
        check=self.checkupcollision()
        if(check==0):
            return 0
        if(manda.get_ycoo()>33):
            return 0
        else:
            self.disappeaar_person()
            self._ycoo-=1
            self.place_on_map()
            return 1

    def jumpdown(self,manda):
        check=self.checkdowncollision()
        if(check==0):
            return 0
        else:
            self.disappeaar_person()
            self._ycoo+=1
            self.place_on_map()
            return 1

    def movedown(self,timenow,manda):
        if(self.get_ycoo()==33):
            self._prevtime=0
            self._skiptime=0.5
            pass
            return 0
        if(self._prevtime==0):
            self._prevtime=timenow
            return 0
        elif(timenow-self._prevtime>self._skiptime):
            self._prevtime=timenow
            self._skiptime*=0.7
            self.jumpdown(manda)
            return 1

    def gravity_reset(self):
        self._prevtime=0
        self._skiptime=0.5