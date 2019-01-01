# 汽车类
class Car():

    def __init__(self,number,color,size):
        self.number = number
        self.color = color
        self.size = size

    def move(self):
        print('车辆启动')

    def stop(self):
        print('车辆熄火')
