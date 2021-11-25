import car
import utime
import _thread
from machine import Pin,Timer
import ble
import bluetooth

quittt=Pin(12,Pin.IN,Pin.PULL_UP)   #调试退出接口，即KEY2

pycar=car.CAR()
carble = bluetooth.BLE()
p = ble.BLESimplePeripheral(carble)
aa=carble.config('mac')
print('mac地址为')
print(aa)

def on_rx(v):
    print(v[0])
    print("Receive_data:", str(v))
    if v[0]==33:
        speed=str(v)[3:-1]
        print(speed)
        pycar.setspeed(int(speed))
    else:
        if v==b'forward':
            pycar.forward()
            pycar.screen()
        elif v==b'backward':
            pycar.backward()
            pycar.screen()
        elif v==b'left':
            pycar.turn_left(1)
            pycar.screen()
        elif v==b'right':
            pycar.turn_right(1)
            pycar.screen()
        elif v==b'stop':
            pycar.stop()
            pycar.screen()
        elif v==b'lighton':
            pycar.light_on()
            pycar.screen()
        elif v==b'lightoff':
            pycar.light_off()
            pycar.screen()
        elif v==b'stop':
            nongsini

p.on_write(on_rx)

def fun(tim):
    pycar.getDistance()
    pycar.getJourney()
    pycar.screen()


while 1:
    if quittt.value()==0:
        print('quit')
        break
    if p.is_connected():
        pycar.s_blue=1
        ds=pycar.getDistance()
        jo=pycar.getJourney()
        pycar.screen()
        print(ds)
        p.notify(str(ds))
    utime.sleep_ms(300)
