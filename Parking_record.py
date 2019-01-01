from Car import Car

# 停车记录类
class Parking_record():

    # 记录车辆信息的方法
    def __init__(self):
        car = Car('','','')
        print('记录成功')

    # 记录车辆进入停车场时间
    def rin_park_time(self,in_park_time):
        print('记录成功')
        return in_park_time

    # 记录车辆离开停车场时间
    def rout_park_time(self,out_park_time):
        print('记录成功')

    # 记录车辆进入车位时间
    def rin_space_time(self,in_space_time):
        print('记录成功')

    # 记录车辆离开车位的时间
    def rout_space_time(self,out_space_time):
        print('记录成功')