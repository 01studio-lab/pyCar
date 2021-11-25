'''
实验名称：pyCar巡线例程
版本：v1.0
日期：2021-11
作者：CaptainJackey
说明：使用pyCar的光电传感器实现黑线巡线
'''

#导入相关模块
from car import CAR
import time

#初始化pyCar
Car = CAR()
time.sleep_ms(300) #等待稳定

'''
########巡线检测###########
T1-T2-T3-T4-T5 光电传感器
11011  直线
10111  偏右，往左调整
01111  严重偏右，往左调整
11101  偏左，往右调整
11110  严重偏左，往右调整
'''

while True:

    if Car.T1()==0 or Car.T2()==0:
        time.sleep_ms(10)
        if Car.T1()==0 or Car.T2()==0 :
            Car.turn_left()
            while Car.T4()==1 and Car.T5()==1:
                if Car.T3() == 0:
                    time.sleep_ms(10)
                    if Car.T3() == 0:
                        break

            Car.forward()

    elif Car.T4()==0 or Car.T5()==0 :
        time.sleep_ms(10)
        if Car.T4()==0 or Car.T5()==0 :
            Car.turn_right()
            while Car.T1()==1 and Car.T2()==1:
                if Car.T3() == 0:
                    time.sleep_ms(10)
                    if Car.T3() == 0:
                        break

            Car.forward()

    else:
        Car.forward()

