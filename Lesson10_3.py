# OOП: Перегрузка операторов
# Обработка ошибок

# class MyException(Exception):
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print('Вызов __str__ метода')
#         if self.message:
#             return f'Моя ошибка {self.message}'
#         else:
#             return 'Исключение Моя Ошибка'
#
#
# raise MyException('Такого значения нет')

# num = input('Введите число ')
# try:
#     num = int(num)
#     print(10/num)  # Ошибка преобразования при вводе букв
#     # raise MyException
# # except Exception as err:
# except ValueError as err:
#     print(err)
# except ZeroDivisionError:
#     print('Делить на 0 нельзя')
# # except TypeError:
# #     print('Ошибка типа')
# finally:
#     print('Всегда выполняется')
#     # raise MyException

# class Test:
#     def __init__(self):
#         print('__init__')
#         self.name = 4
#
#     def __del__(self):
#         print('Удаление')
#
#
# a = Test()
# print(a.name)

# Перегрузка операторов
# class Test:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         print('__add__')
#         return self.number + other
#
#     def __radd__(self, other):
#         print('__radd__')
#         return other + self.number
#
#     def __iadd__(self, other):
#         print('__iadd__')
#         return self.number + other
#
#     def __sub__(self, other):
#         print('__subb__')
#         return self.number - other
#
#     def __rsub__(self, other):
#         print('__rsub__')
#         return other - self.number
#
#     def __isub__(self, other):
#         print('__isub__')
#         return self.number - other
#
#     def __mul__(self, other):
#         print('__mull__')
#         return self.number * other
#
#     def __truediv__(self, other):
#         print('__truediv__')
#         return self.number / other
#
#     def __floordiv__(self, other):
#         print('__floordiv__')
#         return self.number // other
#
#     def __mod__(self, other):
#         print('__mod__')
#         return self.number % other
#
#
# a = Test(5)
# print(a.number + 10)
# print(a + 10)
# print(10 + a)
# a += 10
# print(a)
# print(a - 10)
# print(10 - a)
# a -= 10
# print(a)
# print(a * 5)
# print(a / 10)
# print(a // 10)
# print(a % 10)

class Test:
    @classmethod
    def say(cls):
        print(f'hello say {cls}')

    @property
    def say_hello(self):
        print('hello world')

    @staticmethod
    def say_static():
        print('hello_static')
a = Test()
# a.say()
# Test.say()
# a.say_hello
a.say_static()
Test.say_static()