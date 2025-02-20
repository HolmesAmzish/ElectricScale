import threading
import time
import RPi.GPIO as GPIO


class Hx711(threading.Thread):
    def __init__(self):
        super(Hx711, self).__init__()
        self.setup()  # 初始化GPIO和HX711

    def run(self):
        while True:
            weight = self.startWeight()  # 获取重量数据
            if weight is not None and weight > 3:  # 判断称重是否有效
                print(f"Weight: {weight} grams")
            else:
                print("No valid weight detected.")
            time.sleep(1)  # 每秒钟检测一次

    def setup(self):
        """设置GPIO针脚和初始化变量"""
        self.SCK = 13  # 时钟引脚
        self.DT = 15  # 数据引脚
        self.flag = 1  # 用于首次读数校准
        self.initweight = 0  # 毛重
        self.weight = 0  # 测得的重量
        self.delay = 0.001  # 延时时间，单位秒

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)  # 按物理位置设置GPIO编号
        GPIO.setup(self.SCK, GPIO.OUT)  # 设置SCK为输出
        GPIO.setup(self.DT, GPIO.IN)  # 设置DT为输入
        GPIO.setup(self.DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置内部上拉电阻

    def startWeight(self):
        """读取HX711传感器的数据并返回重量"""
        GPIO.output(self.SCK, 0)
        if GPIO.input(self.SCK):
            time.sleep(self.delay)
        value = 0
        while GPIO.input(self.DT):
            time.sleep(self.delay)

        # 循环读取24位数据
        for i in range(24):
            GPIO.output(self.SCK, 1)
            if (0 == GPIO.input(self.SCK)):
                time.sleep(self.delay)
            value = value << 1  # 左移一位
            GPIO.output(self.SCK, 0)
            if GPIO.input(self.SCK):
                time.sleep(self.delay)
            if GPIO.input(self.DT) == 1:
                value += 1

        GPIO.output(self.SCK, 1)
        GPIO.output(self.SCK, 0)

        # 将读取的原始数据按比例转化为重量
        value = value / 102988  # 校准的特性值

        if self.flag == 1:  # 第一次读取为毛重
            self.flag = 0
            self.initweight = value
        else:
            self.weight = abs(value - self.initweight)  # 当前值减去毛重得到测量重量

        if int(self.weight) >= 0:
            return int(self.weight)
        else:
            return int(self.weight + 324)  # 如果返回值为负，进行校正


# 创建HX711实例并启动线程
hx711 = Hx711()
hx711.start()
