import car
import utime
import _thread
from machine import Pin,Timer

global irremote
irremote=0

#----------IR REMOTE------------
IR_FORWARD=24
IR_BACKWARD=82
IR_LEFT=8
IR_RIGHT=90
IR_STOP=28
IR_LIGHT_ON=22
IR_LIGHT_OFF=13
IR_QUIT=25
IR_SHOW=69

pycar=car.CAR()
#----------test-----------
# #screen
# pycar.screen(0,0,0,0,0,0,0,0,0,0)
# #light
# pycar.light_off()
# #distance
# print(pycar.getDistance())
# #move
# pycar.turn_left(1)
# #count
# print(pycar.getJourney())
#pycar.forward()
utime.sleep(1)

def fun(tim):
    pycar.getDistance()
    pycar.getJourney()
    pycar.screen()

tim = Timer(-1)
#tim.init(period=10000, mode=Timer.PERIODIC,callback=fun)    #周期为10s,当前红外与其他进程会发生冲突  当前是按1就刷新一次
while 1:
    result=pycar.getIR()
    if result!=None:
        print(result)
        if result==IR_FORWARD:
            print('f')
            pycar.forward()
            pycar.screen()
        elif result==IR_BACKWARD:
            print('b')
            pycar.backward()
            pycar.screen()
        elif result==IR_LEFT:
            pycar.turn_left(1)
            pycar.screen()
            print('l')
        elif result==IR_RIGHT:
            pycar.turn_right(1)
            pycar.screen()
            print('r')
        elif result==IR_STOP:
            pycar.stop()
            pycar.screen()
            print('s')
        elif result==IR_LIGHT_ON:
            print('o')
            pycar.light_on()
            pycar.screen()
        elif result==IR_LIGHT_OFF:
            print('f')
            pycar.light_off()
            pycar.screen()
        elif result==IR_QUIT:
            print('Q')
            break
        elif result==IR_SHOW:
            print('S')
            pycar.getDistance()
            pycar.getJourney()
            pycar.screen()
        print(result)



