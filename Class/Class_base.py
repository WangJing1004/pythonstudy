#我就不信学不会
# print("我就不信学不会")
# class Dog:
#     """一次模拟小狗的简单尝试。"""
#     def __init__(self, name, age):
#         """初始化属性name和age。"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """模拟小狗收到命令时蹲下。"""
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         """模拟小狗收到命令时打滚。"""
#         print(f"{self.name} rolled over!")
#
# my_dog = Dog('Willie', 6)
# my_dog.sit()
# my_dog.roll_over()


class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0    #定义属性：self.xxxxx


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.increment_odometer(50)
# print(my_new_car.odometer_reading)
# my_new_car.read_odometer()

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"这台车满电可以跑{range}英里")

class ElectricCar(Car):
    """电动汽车的独特之处。"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  #super.__init__()
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

my_tesls = ElectricCar('tesla', 'model s', 2019)

print(my_tesls.get_descriptive_name())
my_tesls.battery.describe_battery()
my_tesls.battery.get_range()