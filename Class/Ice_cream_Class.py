class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print(f"我是一家餐厅，名字{self.restaurant_name}，"
              f"经营类型是{self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业。")

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name, type)
        self.flavors = ['one', 'two', 'three']
    def Get_IceCream(self):
        print(f'冰激凌的种类分别是: {self.flavors[0]},{self.flavors[1]},{self.flavors[2]}')

ice_creamStand = IceCreamStand('xiaomei', 'ice')
ice_creamStand.Get_IceCream()