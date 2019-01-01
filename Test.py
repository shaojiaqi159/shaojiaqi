# 使用面向对象的思路实现『停车收费』场景：
# 1. 车主开车进入停车场，产生停车记录，
# 2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
# 3. 车主停车完成，
# 一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
# 4. 车主开车离开车位，修改停车记录，
# 5. 车主开车到达出口，系统根据停车的时间生成订单，
# 6. 车主缴纳停车费，
# 7. 车主离开停车场。
# 至此，整个停车收费的场景完成。
import time
from User import User
from Car import Car
from Parking import Parking
from Parking_space import Parking_space
from Order import Order
from Parking_record import Parking_record

# 测试类
class Test():
        if Parking_space.space_all - Parking.car_count == 0:
            print('车位已满，请稍等')
        name = input('请输入姓名')
        phone = input('请输入电话')
        # 创建车主对象
        user = User(name,phone)
        number = input('请输入车牌号')
        color = input('请输入车辆颜色')
        size = input('请输入车辆型号')
        # 创建车对象
        car = Car(number,color,size)
        # 创建停车场对象
        parking = Parking()
        # 打开栏杆
        parking.open()
        # 车主驾驶
        user.drive()
        # 车辆移动
        car.move()
        # 创建停车记录对象，产生停车记录
        parking_record = Parking_record()
        # 记录进入停车场时间
        in_park_time = time.time()
        parking_record.rin_park_time(in_park_time)
        # 进入车位
        parking_space = Parking_space()
        parking_space.in_space()
        # 记录进入车位时间
        in_space_time = time.time()
        parking_record.rin_space_time(in_space_time)
        print('停车完成')
        # 车辆熄火
        car.stop()
        parking.car_count += 1
        Parking_space.space_all -= 1


        car.move()
        # 记录离开车位时间
        out_space_time = time.time()
        parking_record.rout_space_time(out_space_time)
        # 记录停车结束时间
        out_park_time = time.time()
        parking_record.rout_park_time(out_park_time)
        order = Order()
        # 计算停车总时间
        time_all = order.count_time(in_park_time,out_park_time)
        # 计算总费用
        order.count_money(time_all)
        # 车主缴费
        user.pay()
        # 车主离开
        user.drive()



        