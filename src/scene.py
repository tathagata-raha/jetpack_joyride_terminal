import random
import os
from obstacle import Firebeam,Magnet
from config import Config
from board import Board
f=open("log.txt",'a+')
class Scene:

    def __init__(self,board):
        self._floor_val=board.get_height()-2
        self._roof_val=2
        self._width=board.get_width()
        self._grid=board.get_grid()
        self._board=board
        self._obstaclemap=Board(board.get_height(),board.get_width())
        self._firebeamdict={}
        self._magnet=Magnet(0)
    def make(self,board):
        self.initfloorandroof(self._grid)
        self.initobstacles(self._grid)
        self.initcoins(self._grid)
        self.initspeedboost(self._grid)
        # self.initspeedboost(board)

    def initfloorandroof(self,board):
        for i in range(self._width):
            board[self._roof_val][i]=Config.roof
            board[self._floor_val-1][i]=Config.floor
            board[self._floor_val][i]=Config.floor
            
    
    def initobstacles(self,board):
        self._firebeams=[]
        self._firebeamcount=random.randint(10,20)
        for i in range(self._firebeamcount):
            fbeam=Firebeam(random.randint(20,400),random.randint(3,30),random.randint(1,3),random.randint(4,8))
            if(fbeam.get_ycoo()+fbeam.get_length()>35):
                fbeam.set_length(35-fbeam.get_ycoo())
            self._firebeams.append(fbeam)
            self._firebeamdict[str(i)]=[]
            # xco=temp_dict['xco']
            # yco=temp_dict['yco']
            # length=temp_dict['length']
            if(fbeam.get_type()==1):
                for j in range(fbeam.get_length()):
                    board[fbeam.get_ycoo()+j][fbeam.get_xcoo()]=Config.firebeam
                    self._obstaclemap.grid[fbeam.get_ycoo()+j][fbeam.get_xcoo()]=str(i)
                    temp_list=[]
                    temp_list.append(fbeam.get_ycoo()+j)
                    temp_list.append(fbeam.get_xcoo())
                    self._firebeamdict[str(i)].append(temp_list)
            elif(fbeam.get_type()==2):
                for j in range(fbeam.get_length()):
                    board[fbeam.get_ycoo()][fbeam.get_xcoo()+j]=Config.firebeam
                    self._obstaclemap.grid[fbeam.get_ycoo()][fbeam.get_xcoo()+j]=str(i)
                    temp_list=[]
                    temp_list.append(fbeam.get_ycoo())
                    temp_list.append(fbeam.get_xcoo()+j)
                    self._firebeamdict[str(i)].append(temp_list)
            else:
                for j in range(fbeam.get_length()):
                    board[fbeam.get_ycoo()+j][fbeam.get_xcoo()+j]=Config.firebeam
                    self._obstaclemap.grid[fbeam.get_ycoo()+j][fbeam.get_xcoo()+j]=str(i)
                    temp_list=[]
                    temp_list.append(fbeam.get_ycoo()+j)
                    temp_list.append(fbeam.get_xcoo()+j)
                    self._firebeamdict[str(i)].append(temp_list)
            # except:
            #     f.append(xco,yco)
        freex=random.randint(20,200)
        # freex=0
        # freey=0
        # while True:
        #     freey=random.randint(20,400)
        #     freex=random.randint(3,30)
        #     if(board[freex-1][freey-1]==' ' and board[freex-1][freey]==' ' and board[freex-1][freey+1]==' ' and board[freex][freey-1]==' ' and board[freex][freey]==' ' and board[freex][freey+1]==' ' and board[freex+1][freey-1]==' ' and board[freex+1][freey]==' ' and board[freex+1][freey+1]==' '):
        #         break
        # temp=freex
        # freex=freey
        # freey=temp

        self._magnet=Magnet(freex)
        board[2][freex]=Config.magnet
        board[37][freex]=Config.magnet
        board[38][freex]=Config.magnet

    def initcoins(self,board):
        freey=0
        freex=0
        for i in range(15):
            freex=random.randint(20,400)
            freey=random.randint(3,30)
            clength=random.randint(4,20)
            cwidth=random.randint(2,5)
            for j in range(cwidth):
                for k in range(clength):
                    # try:
                    if(board[freey+j][freex+k]==" "):
                        board[freey+j][freex+k]=Config.coin
                    # except:
                    # print(freey,freex,cwidth,clength)

    def initspeedboost(self,board):
        freex=0
        freey=0
        while True:
            freey=random.randint(20,200)
            freex=random.randint(3,30)
            if(board[freex][freey]==' '):
                board[freex][freey]=Config.speedboost
                break

    def delfirebeam(self,ycoo,xcoo):
        char=self._obstaclemap.get_char(ycoo,xcoo)
        for i in self._firebeamdict[char]:
            self._board.del_char_from_map(i[0],i[1])

    def check_magnet(self,manda):
        if(self._magnet.status() and manda.get_xcoo()-self._magnet.get_xcoo()<self._magnet.get_field() and manda.get_xcoo()-self._magnet.get_xcoo()>0 and manda.get_relx()>5):
            return 1
        elif(self._magnet.status() and self._magnet.get_xcoo()-manda.get_xcoo()<self._magnet.get_field() and self._magnet.get_xcoo()-manda.get_xcoo()>0):
            return -1
        else:
            return 0

    def magnet_toggle(self,xcoo):
        if(xcoo+170>self._magnet.get_xcoo() and xcoo<self._magnet.get_xcoo()):
            self._magnet.turnon()
        else:
            self._magnet.turnoff()