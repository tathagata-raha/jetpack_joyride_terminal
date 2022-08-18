class Obstacle:
    def __init__(self,xco,yco):
        self._xco=xco
        self._yco=yco
        self._type=0
    
    def get_xcoo(self):
        return self._xco

    def get_ycoo(self):
        return self._yco
class Firebeam(Obstacle):

    def __init__(self,xco,yco,type1,length):
        Obstacle.__init__(self,xco,yco)
        # self.xco=xco
        # self.yco=yco
        self._type=type1
        self._length=length
        
    def get_length(self):
        return self._length

    def get_type(self):
        return self._type

    def set_length(self,i):
        self._length=i
class Magnet(Obstacle):
    
    def __init__(self,xcoo):
        Obstacle.__init__(self,xcoo,0)
        # self.xco=xcoo
        self._field=50
        self._switch=0


    def get_field(self):
        return self._field

    def turnon(self):
        self._switch=1

    def turnoff(self):
        self._switch=0

    def status(self):
        return self._switch