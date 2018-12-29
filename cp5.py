
import time

class Parking():
    # 假设有100个车位
    parking_space = 100
    # 总停车费用
    parking_money = 0
    # 每小时停车费用30元
    hour_money = 30
    # 存放车辆信息的列表
    car_inf = []
    # 停车时间
    park_time = 0
    # 出车时间
    out_time = 0

    def __init__(self,number,user,phone):
        self.number = number
        self.user = user
        self.phone = phone

    # 停车
    def park(self):
        # 将车位数量减一
        Parking.parking_space -= 1
        # 记录车主停车的时间
        Parking.park_time = time.time()

    # 出车
    @classmethod
    def out(cls):
        cls.park_time = time.time()
        all_time = (cls.out_time - cls.park_time) // 3600
        if all_time == 0.0:
            cls.parking_money = 15
            print('你的停车费为15元')
        else:
            cls.parking_money = all_time * 30
            print('您的停车费为',cls.parking_money,'元')

while True:
    fnc = input(
        '''
        停车每小时30元，不足一小时按半小时收取费用
        1.我要停车
        2.我要离开
        '''
    )

    if fnc == '1':
        if Parking.parking_space == 0:
            print('车位已满')
        else:
            number = input('请输入车牌号')
            user = input('请输入姓名')
            phone = input('请输入电话')
            parking = Parking(number,user,phone)
            parking.park()
            Parking.car_inf.append(number)
            print('OK')
            continue

    if fnc == '2':
        number = input('请输入车牌号')
        while True:
            if number in Parking.car_inf:
                Parking.out()
                print('欢迎下次光临')
            else:
                print('输入有误')
                continue
        

            
