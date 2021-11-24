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
    print(v)
    print("Receive_data:", str(v))
    if v==b'\x00':
        pycar.forward()
        pycar.screen()
    elif v==b'\x00\x00':
        pycar.backward()
        pycar.screen()
    elif v==b'\x00\x00\x00':
        pycar.turn_left(1)
        pycar.screen()
    elif v==b'\x00\x00\x00\x00':
        pycar.turn_right(1)
        pycar.screen()
    elif v==b'\x00\x00\x00\x00\x00':
        pycar.stop()
        pycar.screen()
    elif v==b'\x00\x00\x00\x00\x00\x00':
        pycar.light_on()
        pycar.screen()
    elif v==b'\x00\x00\x00\x00\x00\x00\x00':
        pycar.light_off()
        pycar.screen()
    elif v==b'\x08':
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
