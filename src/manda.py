from main_person import Main_person
from config import Config

class Manda(Main_person):
    def __init__(self,xcoo,ycoo,board,scene):
        Main_person.__init__(self,xcoo,ycoo,2,2,board)
        # self._grid=board.get_grid()
        self._coins=0
        self._relx=0
        self._scene=scene
        self._shield=0
        self._shield_collision=0
        self._boost=0
        self._prevtime=0
        self._skiptime=0.5

    def set_shield(self,i):
        self._shield=i
    def check_shield(self):
        if(self._shield_collision):
            self._shield_collision=0
            return 1
        else:
            return 0
    def get_relx(self):
        return self._relx
    def get_coins(self):
        return self._coins

    def check_boost(self):
        if(self._boost):
            self._boost=0
            return 1
        else:
            return 0
        

    def place_on_map(self):
        if self._shield==0:
            for i in range(self._xcoo,self._xcoo+2):
                self._grid[self._ycoo][i]=Config.mario_head
                self._grid[self._ycoo+1][i]=Config.mario_leg
        else:
            for i in range(self._xcoo,self._xcoo+2):
                self._grid[self._ycoo][i]='\033[0m'+' '
                self._grid[self._ycoo+1][i]='\033[0m'+' '
                self._grid[self._ycoo][i]=Config.mario_shield_head
                self._grid[self._ycoo+1][i]=Config.mario_shield_leg
        
    def shift_manda(self,xcoo):
        if(xcoo==330):
            self.disappeaar_person()
            self.place_on_map()
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0
        else:
            if(self._grid[self._ycoo][self._xcoo+2]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo][self._xcoo+2]==Config.firebeam):
                self.beamcollision(self._ycoo,self._xcoo+2)
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.firebeam):
                self.beamcollision(self._ycoo+1,self._xcoo+2)
            if(self._grid[self._ycoo][self._xcoo+2]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.speedboost):
                self._boost=1
            
            self.disappeaar_person()
            self._xcoo+=1
            self.place_on_map()
            self._relx=self._xcoo-xcoo
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0

    def beamcollision(self,ycoo,xcoo):
        self._scene.delfirebeam(ycoo,xcoo)
        if self._shield:
            self._shield_collision=1
        else:
            self._lives-=1

    def checkupcollision(self):
        if(self._ycoo==3):
            return 0
        else:
            if(self._grid[self._ycoo-1][self._xcoo]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo-1][self._xcoo+1]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo-1][self._xcoo]==Config.firebeam):
                self.beamcollision(self._ycoo-1,self._xcoo)
            elif(self._grid[self._ycoo-1][self._xcoo+1]==Config.firebeam):
                self.beamcollision(self._ycoo-1,self._xcoo+1)
            if(self._grid[self._ycoo-1][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo-1][self._xcoo+2]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo-1][self._xcoo+2]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo-1][self._xcoo+1]==Config.dbullet):
                self._grid[self._ycoo-1][self._xcoo+1]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo-1][self._xcoo]==Config.speedboost):
                self._boost=1
            elif(self._grid[self._ycoo-1][self._xcoo+1]==Config.speedboost):
                self._boost=1
            return 1
    def checkdowncollision(self):
        if(self._ycoo==35):
            return 0
        else:
            if(self._grid[self._ycoo+2][self._xcoo]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo+2][self._xcoo+1]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo+2][self._xcoo]==Config.firebeam):
                self.beamcollision(self._ycoo+2,self._xcoo)
            elif(self._grid[self._ycoo+2][self._xcoo+1]==Config.firebeam):
                self.beamcollision(self._ycoo+2,self._xcoo+1)
            if(self._grid[self._ycoo+2][self._xcoo]==Config.speedboost):
                self._boost=1
            elif(self._grid[self._ycoo+2][self._xcoo+1]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo+2][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo+2][self._xcoo+2]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo+2][self._xcoo+1]==Config.dbullet):
                self._grid[self._ycoo+2][self._xcoo+1]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo+2][self._xcoo+1]='\033[0m'+' '
                self._lives-=1
            return 1
    def checkrightcollision(self):
        if(self._relx==165):
            return 0
        else:
            if(self._grid[self._ycoo][self._xcoo+2]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo][self._xcoo+2]==Config.firebeam):
                self.beamcollision(self._ycoo,self._xcoo+2)
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.firebeam):
                self.beamcollision(self._ycoo+1,self._xcoo+2)
            if(self._grid[self._ycoo][self._xcoo+2]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo][self._xcoo+2]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo+1][self._xcoo+2]==Config.dbullet):
                self._grid[self._ycoo+1][self._xcoo+2]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo][self._xcoo+3]==Config.dbullet):
                self._grid[self._ycoo][self._xcoo+3]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo+1][self._xcoo+3]==Config.dbullet):
                self._grid[self._ycoo+1][self._xcoo+3]='\033[0m'+' '
                self._lives-=1
            return 1
    def checkleftcollision(self):
        if(self._relx==1):
            return 0
        else:
            if(self._grid[self._ycoo][self._xcoo-1]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo+1][self._xcoo-1]==Config.coin):
                self._coins+=1
            if(self._grid[self._ycoo][self._xcoo-1]==Config.firebeam):
                self.beamcollision(self._ycoo,self._xcoo-1)
            if(self._grid[self._ycoo+1][self._xcoo-1]==Config.firebeam):
                self.beamcollision(self._ycoo+1,self._xcoo-1)
            if(self._grid[self._ycoo][self._xcoo-1]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo+1][self._xcoo-1]==Config.speedboost):
                self._boost=1
            if(self._grid[self._ycoo+1][self._xcoo-1]==Config.dbullet):
                self._grid[self._ycoo+1][self._xcoo-1]='\033[0m'+' '
                self._lives-=1
            if(self._grid[self._ycoo][self._xcoo-1]==Config.dbullet):
                self._grid[self._ycoo][self._xcoo-1]='\033[0m'+' '
                self._lives-=1
            return 1

    def stillcheck(self):
        if(self._grid[self._ycoo][self._xcoo+2]==Config.dbullet):
            self._grid[self._ycoo][self._xcoo+2]='\033[0m'+' '
            self._lives-=1
        if(self._grid[self._ycoo+1][self._xcoo+2]==Config.dbullet):
            self._grid[self._ycoo+1][self._xcoo+2]='\033[0m'+' '
            self._lives-=1
    def jump(self):
        check=self.checkupcollision()
        if(check==0):
            return 0
        else:
            self.disappeaar_person()
            self._ycoo-=1
            self.place_on_map()
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0

    def jumpdown(self):
        check=self.checkdowncollision()
        if(check==0):
            return 0
        else:
            self.disappeaar_person()
            self._ycoo+=1
            self.place_on_map()
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0

    def moveright(self):
        check=self.checkrightcollision()
        if(check==0):
            return 0
        else:
            self.disappeaar_person()
            self._xcoo+=1
            self._relx+=1
            self.place_on_map()
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0

    def moveleft(self):
        check=self.checkleftcollision()
        if(check==0):
            return 0
        else:
            self.disappeaar_person()
            self._xcoo-=1
            self._relx-=1
            self.place_on_map()
            if(self._shield_collision):
                self._shield_collision=0
                return 1
            else:
                return 0

    def movedown(self,timenow):
        if(self._ycoo==35):
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
            self.jumpdown()
            return 1

    def gravity_reset(self):
        self._prevtime=0
        self._skiptime=0.5