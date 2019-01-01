# 车位类
class Parking_space():
    # 车位编号
    space_id = ''
    # 车位总数
    space_all = 100
    # 车位状态
    space_state = True

    def in_space(self):
        print('车辆进入车位')
        Parking_space.space_state = False

    def out_space(self):
        print('车辆离开车位')
        Parking_space.space_state = True