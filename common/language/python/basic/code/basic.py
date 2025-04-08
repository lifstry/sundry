#-*- coding:utf-8 -*-

class MyClass:
    # 类变量
    x = 1
    X = 5

    # 构造方法
    def __init__(self, attr_1="obj_attr_1", attr_2="obj_attr_2"):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    @classmethod
    def init(cls, attr_2):
        # python不支持多构造，可以通过这种方式去完成多构造能力。
        return cls("obj_attr_1", attr_2)

    def say(self, words):
        print(words)


MyClass.init("attr_2_value").say("Hello World")
MyClass().say("Hi")

# ----------------------------
print("\n-------------继承---------------\n")


class Animal:
    pass
    # def introduce(self):
    #     print("Animal introduce func")


class Human(Animal):
    pass

    def introduce(self):
        print("Human introduce func")


class Female(Human):
    pass


class Male(Human):
    pass
    # def introduce(self):
    #     print("Male introduce func")


class Work:
    pass
    # def introduce(self):
    #     print("Work introduce func")


class Gentleman(Male, Work):
    pass


# print(Gentleman.__mro__)
Gentleman().introduce()
print(dir(Gentleman()))
print(Gentleman().__class__)
print(type(Gentleman()))

# class Human:
#     # 类变量
#     x = 5

#     def __init__(self, name="张三", age=18):
#         self.name = name
#         self.age = age

#     def say(self, content):
#         print(content)


# class Male(Human):
#     def __init__(self, name="Tom", age=20):
#         # 当子类存在__init__()方法时候，子类将不再自动继承父类的__init__()函数，并会覆盖父类的此函数。
#         # 如果需要保持对父类__init__()的继承，需要显式添加对父类的__init__()调用，如下所示:
#         super().__init__(name, age)
#         # 或者Human.__init(self, name, age)

#         # 子类可以定义自己的属性(也可称为成员变量或实例变量）
#         self.gender = "male"

#     # 也可以定义子类自有方法
#     def work(self):
#         print("male work func")


# if __name__ == "__main__":
#     leo = Male()
#     # leo.say("hello")
#     print(leo.x)

#     # 通过类对象是无法修改类变量的，本质上不再是修改类变量的值，而是在给对象定义新的实例变量。
#     leo.x = 4
#     leo.y = "abc"
#     print(leo.x)
#     print(leo.y)
#     print(Human.x)
#     print("======")
#     print(Male().__class__)
#     print(type(Male()))
