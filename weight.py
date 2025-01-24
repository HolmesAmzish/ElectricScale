import threading
import time

try:
    from RPi import GPIO  # 在树莓派上使用真实的 RPi.GPIO
except ImportError:
    print("RPi.GPIO not available, using MockGPIO instead.")
    import mock_gpio as GPIO

from main import MyWindow


class Hx711(threading.Thread):
    def __init__(self,mywindow):
        super(Hx711, self).__init__()  # 重构run函数必须要写
        self.mywin=mywindow
        self.mywin.initTimer()
        self.mywin.button_open_camera_click()

    def run(self):
        self.setup()
        n=self.startWeight()
        isWeight=False
        while True:
            if (n is not None) and (n>3):
                if not isWeight:
                    self.mywin.camera_capture()
                    self.mywin.getDataInformation()
                    isWeight=True
                    print(n)
                else:
                    n = self.startWeight()
                    print(n)
            else:
                n=self.startWeight()
                isWeight=False
                print(n)


    def getWeight(self):
        n=int(self.weight)
        if n > 0:  # 初始值
            return n

    def setup(self):
        self.SCK = 13  # 物理引脚第11号，时钟
        self.DT = 15  # 物理引脚第13号，数据
        self.flag = 1  # 用于首次读数校准
        self.initweight = 0  # 毛皮
        self.weight = 0  # 测重
        self.delay = 3  # 延迟时间
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        GPIO.setup(self.SCK, GPIO.OUT)  # Set pin's mode is output
        GPIO.setup(self.DT, GPIO.IN)
        GPIO.setup(self.DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def startWeight(self):
        GPIO.output(self.SCK, 0)
        if GPIO.input(self.SCK):
            time.sleep(self.delay)
        value = 0
        while GPIO.input(self.DT):
            time.sleep(self.delay)
        # 循环24次读取数据
        for i in range(24):
            GPIO.output(self.SCK, 1)
            if (0 == GPIO.input(self.SCK)):
                time.sleep(self.delay)
            value = value << 1  # 左移一位，相当于乘2，二进制转十进制
            GPIO.output(self.SCK, 0)
            if GPIO.input(self.SCK):
                time.sleep(self.delay)
            if GPIO.input(self.DT) == 1:
                value += 1
        GPIO.output(self.SCK, 1)
        GPIO.output(self.SCK, 0)
        # return value
        value = value / 102988  # 1905为我传感器的特性值，不同传感器值不同。可先注释此步骤，再去测一物体A得到一个值X,而后用X除以A的真实值即可确定特性值
        if self.flag == 1:  # 第一次读数为毛皮
            self.flag = 0
            self.initweight = value
        else:
            self.weight = abs(value - self.initweight)  # 当前值减毛皮得测量到的重量
        # print(self.weight)
            if(int(self.weight>=0)):
                return int(self.weight)
            else:
                return int(self.weight+324)
