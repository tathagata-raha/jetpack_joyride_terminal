
class Config:
    colors={
        'firebeam' : '\x1b[0;31m',
        'coin' : '\x1b[1;33m',
        'roof' : '\x1b[0;46m',
        'ground' : '\u001b[48;5;94m',
        'magnet' : '\u001b[1;38;5;53;47;1m',
        'head' : '\u001b[0;48;5;202;38;5;20m',
        'leg' : '\u001b[0;38;5;202m' ,
        'shield head' : '\u001b[0;48;5;20;38;5;202m',
        'shield leg' :'\u001b[0;38;5;20m' ,
        'red' : '\u001b[31;1m',
        'green' : '\u001b[32;1m',
        'blue' : '\u001b[0;38;5;39m',
        'boost' : '\u001b[1;48;5;88;38;5;11m',
        'bullet' : '\u001b[0;38;5;20m',
        'dbullet' : '\u001b[0;38;5;87m',
        'grey' : '\u001b[0;38;5;240m'
        # 'eye' : '\u001b[0;38;5;20m'
    }
    END_COLOR = '\033[0m'
    firebeam=colors['firebeam']+'+'+END_COLOR
    # firebeam=colors['Red']+'+'+END_COLOR
    coin=colors['coin']+'$'+END_COLOR
    # coin=colors['Yellow']+'$'+END_COLOR
    # roof=Back.CYAN+'*'
    roof=colors['roof']+' '+END_COLOR
    floor=colors['ground']+' '+END_COLOR
    magnet=colors['magnet']+'M'+END_COLOR
    mario_head=colors['head']+'"'+END_COLOR
    mario_shield_head=colors['shield head']+'"'+END_COLOR
    mario_shield_leg=colors['shield leg']+'|'+END_COLOR
    mario_leg=colors['leg']+'|'+END_COLOR
    disappear_mario=END_COLOR+" "
    shield_not_ready=colors['red']+"SHIELD RECHARGING"+END_COLOR
    shield_ready=colors['green']+"SHIELD READY"+END_COLOR
    shield_on=colors['blue']+"SHIELD ON"+END_COLOR
    shield_disabled=colors['grey']+"SHIELD DISABLED"+END_COLOR
    speedboost=colors['boost']+'>'+END_COLOR
    mbullet=colors['bullet']+'>'+END_COLOR
    dbullet=colors['dbullet']+'<'+END_COLOR
    dragon=colors['firebeam']
    # floor=colors['Water Color']+' '+END_COLOR

class Time:
    def __init__(self,end,blockps,interval):
        self._end=end
        self._blockps=blockps
        self._interval=interval
        self._boostmode=0

    def get_end(self):
        return self._end

    def get_blockps(self):
        return self._blockps

    def get_interval(self):
        return self._interval

    def get_boost(self):
        return self._boostmode

    def boost(self,timenow):
        self._end=timenow+(self._end-timenow)/2
        self._blockps*=2
        self._interval/=2
        self._boostmode=1