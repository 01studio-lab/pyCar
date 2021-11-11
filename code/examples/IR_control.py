'''
实验名称：使用红外遥控器控制pyCar
版本：v1.0
日期：2021-11
作者：CaptainJackey
说明：将文件改成main.py发送到pyCar可离线运行
'''

#导入相关模块
from car import CAR
import time

#初始化pyCar
Car = CAR()
time.sleep_ms(300) #等待稳定

#车灯状态
light_state = 0 

while True:
    
    key = Car.getIR() #读取红外传感器

    if key != None: #有按键按下
        
        #按键上，前进
        if key == 24:
            
            Car.forward()
            time.sleep(1)
            Car.stop()
        
        #按键下，后退
        if key == 82:
            
            Car.backward()
            time.sleep(1)
            Car.stop()

        #按键左，左转
        if key == 8:
            
            Car.turn_left(mode=1)
            time.sleep_ms(250)
            Car.stop()

        #按键右，右转
        if key == 90:
            
            Car.turn_right(mode=1)
            time.sleep_ms(250)
            Car.stop()                                            
        
        #按键OK，车灯开关
        if key == 28: 
            
            light_state = not light_state
            Car.light(light_state)
