# The MIT License (MIT)
#
# Copyright (c) 2021 , 01Studio

from machine import Pin,PWM
import time

#编码盘计数
count1 = 0

class CAR():
    
    #初始化
    def __init__(self):
        
        #电机1
        self.M1_P = PWM(Pin(14), freq=1000, duty=0) 
        self.M1_N = PWM(Pin(15), freq=1000, duty=0)
        
        #电机2
        self.M2_P = PWM(Pin(16), freq=1000, duty=0) 
        self.M2_N = PWM(Pin(17), freq=1000, duty=0)
        
        #电机3
        self.M3_P = PWM(Pin(18), freq=1000, duty=0) 
        self.M3_N = PWM(Pin(19), freq=1000, duty=0)

        #电机4
        self.M4_P = PWM(Pin(21), freq=1000, duty=0) 
        self.M4_N = PWM(Pin(22), freq=1000, duty=0)

        #车灯      
        self.light = Pin(5, Pin.OUT)

        #超声波测距
        self.trig = Pin(27,Pin.OUT)
        self.echo = Pin(26,Pin.IN)
        
        #编码盘测速
        self.speed = Pin(4,Pin.IN,Pin.PULL_UP)
        self.speed.irq(self.speed_count,Pin.IRQ_FALLING)
        
        #巡线传感器初始化，五路光电
        self.t1 = Pin(33, Pin.IN, Pin.PULL_UP)
        self.t2 = Pin(34, Pin.IN, Pin.PULL_UP)
        self.t3 = Pin(35, Pin.IN, Pin.PULL_UP)
        self.t4 = Pin(36, Pin.IN, Pin.PULL_UP)
        self.t5 = Pin(39, Pin.IN, Pin.PULL_UP)
        
        #红外接收头
        self.IR = Pin(32, Pin.IN)
        
    
    #前进
    def forward(self):
        
        self.M1_P.duty(1023)
        self.M1_N.duty(0)    
        self.M2_P.duty(1023)
        self.M2_N.duty(0)
        self.M3_P.duty(1023)
        self.M3_N.duty(0)
        self.M4_P.duty(1023)
        self.M4_N.duty(0)
    
    #后退
    def backward(self): 

        self.M1_P.duty(0)
        self.M1_N.duty(1023)    
        self.M2_P.duty(0)
        self.M2_N.duty(1023)
        self.M3_P.duty(0)
        self.M3_N.duty(1023)
        self.M4_P.duty(0)
        self.M4_N.duty(1023)

    #左转
    def turn_left(self, mode=0):
        
        #普通转向
        if mode == 0: 
            self.M1_P.duty(0)
            self.M1_N.duty(0)    
            self.M2_P.duty(1023)
            self.M2_N.duty(0)
            self.M3_P.duty(1023)
            self.M3_N.duty(0)
            self.M4_P.duty(0)
            self.M4_N.duty(0)
        
        #大幅度转向
        elif mode ==1:
            self.M1_P.duty(0)
            self.M1_N.duty(1023)    
            self.M2_P.duty(1023)
            self.M2_N.duty(0)
            self.M3_P.duty(1023)
            self.M3_N.duty(0)
            self.M4_P.duty(0)
            self.M4_N.duty(1023)

    #右转
    def turn_right(self, mode=0): 

        #普通转向
        if mode == 0:
            self.M1_P.duty(1023)
            self.M1_N.duty(0)    
            self.M2_P.duty(0)
            self.M2_N.duty(0)
            self.M3_P.duty(0)
            self.M3_N.duty(0)
            self.M4_P.duty(1023)
            self.M4_N.duty(0)
        #大幅度转向
        elif mode == 1: 
            self.M1_P.duty(1023)
            self.M1_N.duty(0)    
            self.M2_P.duty(0)
            self.M2_N.duty(1023)
            self.M3_P.duty(0)
            self.M3_N.duty(1023)
            self.M4_P.duty(1023)
            self.M4_N.duty(0)

    #停止
    def stop(self): 
        self.M1_P.duty(0)
        self.M1_N.duty(0)    
        self.M2_P.duty(0)
        self.M2_N.duty(0)
        self.M3_P.duty(0)
        self.M3_N.duty(0)
        self.M4_P.duty(0)
        self.M4_N.duty(0)
    
    #打开车头灯
    def light_on(self):
        
        self.light.on()
    
    #关闭车头灯
    def light_off(self):
        
        self.light.off()
    
    #车头灯引脚输出
    def light(self,value):
        
        if value == 0:
            self.light.off()
        elif value == 1:
            self.light.on()

    #超声波测距
    def getDistance(self):
        distance=0
        self.trig.value(1)
        time.sleep_us(20)
        self.trig.value(0)
        while self.echo.value() == 0:
            pass
        if self.echo.value() == 1:
            ts=time.ticks_us()            #开始时间
            while self.echo.value() == 1: #等待脉冲高电平结束
                pass
            te=time.ticks_us()            #结束时间
            tc=te-ts                      #回响时间（单位us，1us=1*10^(-6)s）
            distance=(tc*170)/10000       #距离计算 （单位为:cm）
            
        return distance

    #编码盘测速计数
    def speed_count(self,args):
        
        global count1
        count1 = count1+1

    #返回行驶路程 
    def getJourney(self):     
        
        global count1
        return '%.2f'%(count1/20*0.188)
    
    #路程清0
    def journey_clear(self):       
        
        global count1
        count1 = 0    

    #五路光电传感器
    def T1(self):
        
        return self.t1.value()

    def T2(self):
        
        return self.t2.value()
    
    def T3(self):
        
        return self.t3.value()

    def T4(self):
        
        return self.t4.value()
    
    def T5(self):
        
        return self.t5.value()

    #红外接收解码
    def getIR(self):

        if (self.IR.value() == 0):
            count = 0
            while ((self.IR.value() == 0) and (count < 100)): #9ms
                count += 1
                time.sleep_us(100)
            if(count < 10):
                return None
            count = 0
            while ((self.IR.value() == 1) and (count < 50)): #4.5ms
                count += 1
                time.sleep_us(100)
                
            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while ((self.IR.value() == 0) and (count < 10)):    #0.56ms
                    count += 1
                    time.sleep_us(100)

                count = 0
                while ((self.IR.value() == 1) and (count < 20)):   #0: 0.56mx
                    count += 1                                #1: 1.69ms
                    time.sleep_us(100)

                if count > 7:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1

            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
                return data[2]
            else:
                return("REPEAT")
