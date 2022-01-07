'''
实验名称：使用红外遥控器控制pyCar（麦克纳姆轮）
版本：v1.0
日期：2021-12
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
        
        #按键2，前移
        if key == 0x46:
            
            Car.up()
            time.sleep(1)
            Car.stop()
        
        #按键8，后移
        if key == 0x15:
            
            Car.down()
            time.sleep(1)
            Car.stop()

        #按键4，左移
        if key == 0x44:
            
            Car.left()
            time.sleep(1)
            Car.stop()

        #按键6，右移
        if key == 0x43:
            
            Car.right()
            time.sleep(1)
            Car.stop()

        #按键1，左前移
        if key == 0x45:
            
            Car.up_left()
            time.sleep(1)
            Car.stop()   

        #按键3，右前移
        if key == 0x47:
            
            Car.up_right()
            time.sleep(1)
            Car.stop()

        #按键7，左后移
        if key == 0x07:
            
            Car.down_left()
            time.sleep(1)
            Car.stop()

        #按键9，右后移
        if key == 0x09:
            
            Car.down_right()
            time.sleep(1)
            Car.stop()

        #按键*，逆时针旋转
        if key == 0x16:
            
            Car.Counterclockwise()
            time.sleep(1)
            Car.stop()   

        #按键#，顺时针旋转
        if key == 0x0d:
            
            Car.clockwise()
            time.sleep(1)
            Car.stop()
            
        #按键OK，车灯开关
        if key == 28: 
            
            light_state = not light_state
            Car.light(light_state)
