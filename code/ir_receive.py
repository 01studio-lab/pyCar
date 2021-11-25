from machine import Pin
from time import ticks_us,ticks_diff

class IRrec:
    def __init__(self, pin=32):
        self._ic_start = 0                                #每一个信号的开始时间
        self._ic_last  = 0                                #每一t信号的结束时间
        self._ic_width = 0                                #每一个信号的宽度
        self._sr       = [0x00, 0x00, 0x00, 0x00]         #整个红外信号的结构[地址，地址反码，命令，命令反码]
        self._address  = 0                                #红外地址
        self._command  = 0                                #红外命令
        self._cb       = 0                                #递归？？取出地址和命令值
        self._ic_pin   = Pin(pin, Pin.IN)
        self._ic_pin.irq(trigger=Pin.IRQ_RISING, handler=self._ic_cb)     #每次信号中断触发_ic_cb函数
        self._id       = 0                                #信号个数（计数用，暂时程序里没有用到）
        self._rst()                                       #各项数据清零

    def _rst(self):
        self._sr       = [0x00, 0x00, 0x00, 0x00]
        self._ic_last  = ticks_us()
        self._sc       = 0
        self._sb       = 0

    def _bit(self, v):               
        self._sr[self._sb] = (self._sr[self._sb] >> 1)|(v << 8)
        self._sc += 1
        if (self._sc > 7):
            self._sc = 0
            self._sb += 1
            if (self._sb > 3):
                if ((self._sr[0] ^ self._sr[1] ^ self._sr[2] ^ self._sr[3]) == 0):#异或校验2组数据完整性 根据红外协议来讲 没问题pass 有问题清空重新来过
                    self._address = self._sr[0]
                    self._command = self._sr[2]
                    if (self._cb):
                        self._cb(self, self._address, self._command)
                self._rst()

    def _ic_cb(self, pin):

        self._ic_start = ticks_us()#时间
        icw = ticks_diff(self._ic_start, self._ic_last)
        self._ic_last = self._ic_start
        self._ic_width = icw
        self._id += 1
        if (icw > 5500):
            pass
        elif (icw > 4000):#一个高低信号 大于 4ms  4.5ms 是发送结束 和起始
            self._rst()
        elif (icw > 2500):  # Repeat command#一个高低信号 大于 2.5ms 结束码2.5ms   收到 结束信号直接结束
            pass
        elif (icw > 1500):#一个高低信号 大于 1.5ms     有效信号处理
            self._bit(1)  # High bit
        else:
            self._bit(0)  # Low bit#低8位  小于 1.5ms的 有效信号处理
            # print('Low bit')
            
        
    def callback(self, fn):
        self._cb = fn
        

def nec_cb(nec, a, c):
    print(a, c)

from ir_receive import IRrec
nec = IRrec(35)
nec.callback(nec_cb)
