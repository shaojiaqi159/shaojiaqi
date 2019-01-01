
# 订单类
class Order():
    # 订单编号
    order_id = ''
    # 每小时停车费
    money_hour = 5

    # 计算停车总时间的方法
    def count_time(self,in_time,out_time):
        self.in_time = in_time
        self.out_time = out_time
        time_all = out_time - in_time
        return time_all

    # 统计停车总费用的方法
    def count_money(self,time_all):
        self.time_all = time_all
        if self.time_all <= 3600:
            print('您的停车费用为5元')
        elif self.time_all > 3600 and time_all % 3600 != 0:
            all_money = (self.time_all // 3600 + 1) * 5
            print('您的停车费用为' + str(all_money) + '元')
        else:
            all_money = (self.time_all / 3600) * 5
            print('您的停车费用为' + str(all_money) + '元')