# class Person:
#     def __new__(cls, *args, **kwargs):
#         print('метод __new__')
#         #  Вызываем неизмененный метод __new__
#         return super(Person, cls).__new__(cls)
#
#     def __init__(self):
#         print('метод __init__')
#
#
# person1 = Person()
# person2 = Person()

# class Car:
#     # def __init__(self, color):
#     #     self.color = color
#
#     def say_hello(self):
#         print('hello')
#
#
# class Auto(Car):
#     # def __init__(self, color, speed):
#     #     super().__init__(color)
#     #     self.speed = speed
#
#     def say_speed(self):
#         # print(f'{self.speed=}')
#         print('speed')
#
#
# class Bus(Car, Auto):
#     # def __init__(self, color, seed):
#     #     super().__init__(color)
#     #     self.seed = seed
#
#     def say_seed(self):
#         # print(f'{self.seed=}')
#         print('seed')


# car1 = Car('yellow')
# # print(car1.color)
#
# car2 = Auto('black', 100)
# # print(car2.color, car2.speed)
#
# car3 = Bus('yellow', 34, 100)
# # print(car3.color, car3.seed)
# car1.say_hello()
#
# car2.say_hello()
# car2.say_speed()
#
# car3.say_hello()
# car3.say_seed()
# car3.say_speed()

# a = Bus()
# a.say_hello()

# class Test:
#     _name = 'Иван'
#
#     def _say_name(self):
#         print(f'{self._name=}')

# class Test:
#     __name = 'Иван'
#
#     def __say_name(self):
#         print('hello')
#
#     # def say_name_too(self):
#     #     print(self.__name)
#
# a = Test()
# # a.__say_name()
# # print(a.__name)
# # a.say_name_too()
# print(a._Test__name)
# a._Test__say_name()

# class Person:
#     def say_hello(self):
#         print('hello')
#
#
# class Person2(Person):
#     def say_hello(self):
#         print('buy')
#
#
# a = Person2()
# a.say_hello()

# class Test(list):
#     # def reverse_list(self):
#     #     if len(self) > 2:
#     #         list1 = self.reverse()
#     #         # return self[::-1]
#     #         return list1
#     #     else:
#     #         self.pop()
#     def __len__(self):
#         print('Длинна')
#         return super().__len__()
#
#
# a = Test()
# a.append(1)
# a.append(2)
# a.append(4)
#
# print(len(a))
# print(a)
# a.reverse_list()
# print(a)
# print(len(a))

class Test:
    def __call__(self, n, *args, **kwargs):
        print(f'{args}')
        print(f'{kwargs}')
        print(n)


a = Test()
a(1, 2, 3, z=5)
