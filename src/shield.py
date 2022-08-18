import time
class Shield:
    def __init__(self):
        self._sttime=time.time()
        self._status=0
        self._actime=0
    
    def get_sttime(self):
        return self._sttime

    def get_status(self):
        return self._status

    def get_actime(self):
        return self._actime

    def ready(self):
        self._status=1

    def activate(self,manda):
        self._status=2
        self._actime=time.time()
        manda.set_shield(1)

    def deactivate(self,manda):
        self._sttime=time.time()
        self._status=0
        self._actime=0
        manda.set_shield(0)

    def disable(self):
        self._status=4

    