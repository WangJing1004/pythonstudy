# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def describe_user(self):
#         print(f"姓是：{self.first_name},名是{self.last_name}")
#
#     def Greet_user(self):
#         print(f"{self.first_name}您好，欢迎光临！")
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name, age)
#         self.privileges = ["can add post" ,"can delete post" ,"can ban user"]
#     def show_privileges(self):
#         print(f"{self.first_name}的权限是{self.privileges}")
#
# admin = Admin('wang', 'jing', 28)
# admin.show_privileges()

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"姓是：{self.first_name}, 名是：{self.last_name}")

    def greet_user(self):
        print(f"{self.first_name}您好，欢迎光临！")


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)  # 修正这里
        self.privileges = ["可以添加帖子", "可以删除帖子", "可以禁止用户"]

    def show_privileges(self):
        print(f"{self.first_name}的权限是: {', '.join(self.privileges)}")


admin = Admin('wang', 'jing', 28)
admin.describe_user()   # 可选：描述用户
admin.greet_user()      # 可选：问候用户
admin.show_privileges()  # 显示管理员权限