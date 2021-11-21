import car
import utime
import _thread

IR_FORWARD=24
IR_BACKWARD=82
IR_LEFT=8
IR_RIGHT=90
IR_STOP=28
IR_LIGHT_ON=22
IR_LIGHT_OFF=13
IR_SHOW=25

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
        
while 1:
    result=pycar.getIR()
    if result!=None:
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
        elif result==IR_SHOW:
            print('S')
            pycar.getDistance()
            pycar.getJourney()
            pycar.screen()
            break
        print(result)


