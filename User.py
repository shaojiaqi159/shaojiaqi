# 车主类
class User():

    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def drive(self):
        print('车主驾驶汽车')

    def pay(self):
        print('车主缴费')
