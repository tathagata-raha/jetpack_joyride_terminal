import time
import random
from config import Config
class Bullet:
    def __init__(self,board,dir,scene,dragon):
        self._grid=board.get_grid()
        self._dir=dir
        self._bulletc=0
        self._bulletlist=[]
        self._scene=scene
        self._enemy=dragon
        self._prevtime=0

    def disappear(self,ycoo,xcoo,char):
        self._grid[ycoo][xcoo]=' '+'\033[0m'
        self._grid[ycoo][xcoo]=char

    

    def delete_bullet(self,i):
        bullet=self._bulletlist[i]
        self._grid[bullet['ycoo']][bullet['xcoo']]=' '+'\033[0m'
        self._grid[bullet['ycoo']][bullet['xcoo']]=bullet['prevchar']
        del self._bulletlist[i]
        self._bulletc-=1

    def place_on_map(self,ycoo,xcoo):
        if(self._grid[ycoo][xcoo]==Config.magnet or self._grid[ycoo][xcoo]==Config.magnet or self._grid[ycoo][xcoo]==Config.speedboost or self._grid[ycoo][xcoo]==Config.firebeam or self._grid[ycoo][xcoo]==Config.coin):
            temp=self._grid[ycoo][xcoo]
        else:
            temp=" "
        if(self._dir==1):
            self._grid[ycoo][xcoo]=Config.mbullet
        else:
            self._grid[ycoo][xcoo]=Config.dbullet
        return temp



class Mandabullet(Bullet):
    def __init__(self,board,scene,dragon):
        Bullet.__init__(self,board,1,scene,dragon)
        self._interval=0.1

    def eject(self,manda):
        timenow=time.time()
        if(timenow-self._prevtime<1):
            return
        self._prevtime=timenow
        dict={}
        dict['xcoo']=manda.get_xcoo()+2
        dict['ycoo']=manda.get_ycoo()
        dict['etime']=timenow
        dict['active']=1
        dict['relx']=manda.get_relx()+2
        dict['prevchar']=' '
        self._bulletlist.append(dict)
        self._bulletc+=1
    

    def printlist(self):
        print(self._bulletlist)
    def checkcollision(self,ycoo,xcoo):
        check=0
        if(self._grid[ycoo][xcoo+1]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo+1)
            check=1
        elif(self._grid[ycoo][xcoo+2]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo+2)
            check=1
        elif(self._grid[ycoo][xcoo+3]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo+3)
            check=1
        elif(self._grid[ycoo][xcoo+4]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo+4)
            check=1
        if((self._enemy.get_ycoo()-ycoo<2 and self._enemy.get_ycoo()-ycoo>-4) and self._enemy.get_xcoo()-xcoo<4):
            self._enemy.lose_life()
            check=1
        return check
    def bullet_handler(self):
        timenow=time.time()
        for i in self._bulletlist:
            if(i['relx']<165 and i['xcoo']<495):
                if(i['active']==1 and (timenow-i['etime'])>self._interval):
                    i['etime']=timenow
                    self.disappear(i['ycoo'],i['xcoo'],i['prevchar'])
                    check_col=self.checkcollision(i['ycoo'],i['xcoo'])
                    if(check_col==0):
                        i['xcoo']+=4
                        i['relx']+=4
                        char=self.place_on_map(i['ycoo'],i['xcoo'])
                        i['prevchar']=char
                    else:
                        i['active']=0
            else:
                i['active']=0
        for i in range(self._bulletc):
            if(self._bulletlist[i]['active']==0):
                self.delete_bullet(i)
                break

class Dragonbullet(Bullet):
    def __init__(self,board,scene,manda):
        Bullet.__init__(self,board,2,scene,manda)
        self._interval=0.1

    def eject(self,dragon):
        timenow=time.time()
        if(timenow-self._prevtime<1):
            return
        self._prevtime=timenow
        dict={}
        dict['xcoo']=dragon.get_xcoo()-1
        dict['ycoo']=random.randint(dragon.get_ycoo(),dragon.get_ycoo()+3)
        dict['etime']=timenow
        dict['active']=1
        dict['relx']=dragon.get_xcoo()
        dict['prevchar']=' '
        dict['check']=0
        self._bulletlist.append(dict)
        self._bulletc+=1

    def checkcollision(self,ycoo,xcoo):
        check=0
        if(self._grid[ycoo][xcoo-1]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo-1)
            check=1
        elif(self._grid[ycoo][xcoo-2]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo-2)
            check=1
        elif(self._grid[ycoo][xcoo-3]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo-3)
            check=1
        elif(self._grid[ycoo][xcoo-4]==Config.firebeam):
            self._scene.delfirebeam(ycoo,xcoo-4)
            check=1
        # if((self._enemy.get_ycoo()-ycoo<1 and self._enemy.get_ycoo()-ycoo>-2) and xcoo-self._enemy.get_xcoo()<4):
        #     self._enemy.lose_life()
        #     check=1
        return check

    def bullet_handler(self):
        timenow=time.time()
        for i in self._bulletlist:
            if(i['xcoo']>330):
                if(i['active']==1 and (timenow-i['etime'])>self._interval and (self._grid[i['ycoo']][i['xcoo']]==Config.dbullet or i['check']==0)):
                    if(i['check']==0):
                        i['check']=1
                    i['etime']=timenow
                    self.disappear(i['ycoo'],i['xcoo'],i['prevchar'])
                    check_col=self.checkcollision(i['ycoo'],i['xcoo'])
                    if(check_col==0):
                        i['xcoo']-=1
                        char=self.place_on_map(i['ycoo'],i['xcoo'])
                        i['prevchar']=char
                    else:
                        i['active']=0
            else:
                i['active']=0
        for i in range(self._bulletc):
            if(self._bulletlist[i]['active']==0):
                self.delete_bullet(i)
                break

    

