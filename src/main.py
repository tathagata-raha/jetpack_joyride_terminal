import os
import signal
from board import Board
from scene import Scene
from manda import Manda
from dragon import Dragon
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from shield import Shield
from config import Time
from bullet import Mandabullet,Dragonbullet
import time
import math
board = Board(40,500)
scene=Scene(board)
scene.make(board)
manda=Manda(3,35,board,scene)
dragon=Dragon(485,33,board,scene)
manda.place_on_map()
stime=time.time()
mbullet=Mandabullet(board,scene,dragon)
dbullet=Dragonbullet(board,scene,manda)
timec=Time((board.get_width()-170)/2, 2,0.5)
shield=Shield()
etime=0
def gameover(message):
    os.system('clear')
    print("Score:" + str(manda.get_coins()))
    print(message)
    quit()
def movemanda():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.05):
        ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    char = user_input()
    if char == 'q':
        # os.system("killall afplay")
        gameover("You quit the game!!!")

    # if char == 'p':
    #     # os.system("killall afplay")
    #     print(scene.obstaclemap.print_it(0,0,0))
    #     quit()
    
    if char == 'w':
        shield_check=manda.jump()
        dragon.jump(manda)
        if(shield_check):
            shield.deactivate(manda)
        return 3
    if char == 's':
        shield_check=manda.jumpdown()
        dragon.jumpdown(manda)
        if(shield_check):
            shield.deactivate(manda)
        return 1
    if char == 'd':
        shield_check=manda.moveright()
        if(shield_check):
            shield.deactivate(manda)
        return 1
    if char == 'a':
        shield_check=manda.moveleft()
        if(shield_check):
            shield.deactivate(manda)
        return 1
    if char == ' ':
        if(manda.get_xcoo()>330):
            shield.disable()
        if(shield.get_status()==1):
            shield.activate(manda)
    if char == 'p':
        mbullet.eject(manda)

    if char == 'o':
        mbullet.printlist()
        quit()
    return 2
prev=0
while True:
    timenow=time.time()-stime
    if(manda.get_lives()<=0):
        gameover("No lives left!!!")
    if(dragon.get_lives()<=0):
        gameover("Congrats!!!You wom.")
    mbullet.bullet_handler()
    if(manda.get_xcoo()>320):
        dbullet.eject(dragon)
        dbullet.bullet_handler()
        manda.stillcheck()
    retvar=movemanda()
    movecheck=0
    if(retvar!=3):
        movecheck=manda.movedown(timenow)
        dragon.movedown(timenow,manda)
    else:
        manda.gravity_reset()
        dragon.gravity_reset()
    check_magnet=0
    check_magnet=scene.check_magnet(manda)
    if(check_magnet==1):
        manda.moveleft()
    elif(check_magnet==-1):
        manda.moveright()
    if(shield.get_status()==0 and time.time()-shield.get_sttime()>60):
        shield.ready()
    if(shield.get_status()==2 and time.time()-shield.get_actime()>10):
        shield.deactivate(manda)
    if(retvar==1 or retvar==3 or movecheck==1 or check_magnet==1 or check_magnet==-1):
        os.system('clear')
        if(timenow<timec.get_end()):
            if(manda.check_boost()):
                timec.boost(timenow)
            # if(timec.get_boost()):
            #     shield_check=manda.shift_manda(330)
            #     if(shield_check):
            #         shield.deactivate(manda)
            scene.magnet_toggle(math.floor(timenow*timec.get_blockps()))
            if(timec.get_boost()==0):
                board.print_it(math.floor(timenow*timec.get_blockps()),manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
                prev=math.floor(timenow*timec.get_blockps())
            else:
                board.print_it(math.floor(prev+(timenow*2-prev)*timec.get_blockps()),manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
        else:
            shield_check=manda.shift_manda(330)
            if(shield_check):
                shield.deactivate(manda)
            if(manda.check_boost()):
                timec.boost(timenow)
            if(timec.get_boost()):
                shield_check=manda.shift_manda(330)
                if(shield_check):
                    shield.deactivate(manda)
            scene.magnet_toggle(330)
            board.print_it(330,manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
    timenow=time.time()-stime
    # if(retvar!=3):
    #     movecheck=manda.movedown(time.time())
    if(timenow-etime>timec.get_interval()):
        etime=timenow
        os.system('clear')
        if(etime<timec.get_end()):
            # if(movecheck==0):
            shield_check=manda.shift_manda(math.floor(etime*timec.get_blockps()))
            if(shield_check):
                shield.deactivate(manda)
            if(manda.check_boost()):
                timec.boost(timenow)
            if(timec.get_boost()):
                shield_check=manda.shift_manda(math.floor(etime*timec.get_blockps()))
                if(shield_check):
                    shield.deactivate(manda)
            scene.magnet_toggle(math.floor(etime*timec.get_blockps()))
            if(timec.get_boost()==0):
                board.print_it(math.floor(etime*timec.get_blockps()),manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
                prev=math.floor(etime*timec.get_blockps())
            else:
                board.print_it(math.floor(prev+(etime*2-prev)*timec.get_blockps()),manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
        else:
            # if(movecheck==0):
            shield_check=manda.shift_manda(330)
            if(shield_check):
                shield.deactivate(manda)
            if(manda.check_boost()):
                timec.boost(timenow)
            scene.magnet_toggle(330)
            board.print_it(330,manda.get_coins(),manda.get_lives(),shield.get_status(),dragon.get_lives())
