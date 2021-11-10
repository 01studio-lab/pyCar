# pyCar
由01Studio发起的MicroPython开源小车。

## 项目简介
Micropython是指使用python做各类嵌入式硬件设备编程。MicroPython发展势头强劲，01Studio一直致力于Python嵌入式编程，特此推出pyCar开源项目，旨在让MicroPython变得更加流行。使用MicroPython，你可以轻松地实现小车的前进、后台、巡线、避障、红外遥控等功能。

例：
```python
#构建小车对象
from car import CAR
Car = CAR()

#使用方法示例
Car.forward() #前进

Car.backward() #后退

Car.turn_left() #左转

Car.turn_right() #右转

Car.light_on() #打开车头灯

...
```

## 硬件资源
● 主控：ESP32-WROOM-32 （Flash:4MBytes）支持WiFi/BLE  
● 4 x TT马达。支持PWM调速  
● 2 x 编码盘测速  
● 5 x 光电传感器，用于巡线  
● 1 x 超声波传感器，用于避障  
● 1 x 0.96寸OLED显示屏  
● 1 x 红外遥控  
● 2 x 车头草帽灯（可控制）  
● 2 x 车尾灯（常亮）  
● 2 x 按键  
● 1 x LED  
● 1 x 锂电池座18650（带充电电路）  


## 贡献说明
本项目预设以下文件夹：

### code
项目代码，包含主要代码car.py和其它示例代码。

### docs
pyCar官方说明文档、MicroPython库文档。

### firmware
pyCar的MicroPython固件。

### hardware
硬件资料，原理图、尺寸图等。

### update.md
更新日志。

## 贡献用户
【CaptainJacky】 pyCar项目发起人，负责硬件和MicroPython软件设计。

欢迎参与项目贡献！

## 联系方式
jackey@01studio.cc