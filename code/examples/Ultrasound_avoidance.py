'''
实验名称：pyCar超声波避障
版本：v1.0
日期：2021-11
作者：CaptainJackey
说明：将文件改成main.py发送到pyCar可离线运行
'''

#导入相关模块
from car import CAR
import time,random

#初始化pyCar
Car = CAR()
time.sleep_ms(300) #等待稳定

turn_node = 1

while True:


    #距离少于50cm就转弯
    if 0 < int(Car.getDistance()) < 50 :
        
        #从0和1中随机生成一个数决定左右转向
        if turn_node == 1:
            
            turn_direct = random.randint(0,1)
            turn_node = 0
        
        #1右转，0左转。
        if turn_direct:
            
            Car.turn_right(mode=1)
            
        else:
            
            Car.turn_left(mode=1)
        
    else: #走直线
        
        Car.forward()
        turn_node = 1
        
    time.sleep_ms(50) #适当延时调整响应速度
