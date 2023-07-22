# Декораторы

# О функциях

# def func():
#     pass
# print(type(func))

# Присвоение функции переменной
# def hello():
#     print('hello world')
#
#
# x = hello
# print(type(x))
# # <class 'function'>
# x()
# hello world

# функция обертка
# def wrapper_function():
#     print('wrapper')
#
#     def func():
#         print('func')
#         print('Hello')
#
#     func()
#     print('wrapper')
#
#
# wrapper_function()

# Передача функции в виде аргумента
# def hello():
#     print('hello world')
#
#
# def func1(func):
#     print(f'Получена функция {func} в качестве аргумента')
#     # func()
#     return func
#
#
# func1(hello)()

# Декоратор
# Простой декоратор
# def null_decorator(func):
#     return func


# # обернем им другую функцию
# def greet():
#     return 'Hello'
#
#
# greet = null_decorator(greet)
# print(greet())

# Аналогично можно записать через @
# @null_decorator
# def greet():
#     return 'Hello!'
#
#
# print(greet())

# Изменение поведения функции
# def uppercase(func):
#     def wrapper():  # Замыкание
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#
#     return wrapper
#
#
# @uppercase
# def greet():
#     return 'Hello!'
#
#
# print(greet())
# # HELLO!
# print(greet)
# #<function uppercase.<locals>.wrapper at 0x0000017CC0B04720>

# Пример декоратора из лекции
# def hello():
#     print('hello world')


# def decorator_func(func):
#     def wrapper():
#         print('Функция обертка')
#         print(f'Оборачиваемая функция {func}')
#         print('Выполняемая функция')
#         func()
#         print('Выходим из обертки')
#
#     return wrapper
#
#
# # hello = decorator_func(hello)
# # hello()
#
# @decorator_func
# def hello():
#     print('hello world')
#
#
# hello()
# import time
# from urllib.request import urlopen
#
#
# def dec_fun(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Время выполнения функции {end - start}')
#
#     return wrapper
#
#
# @dec_fun
# def func1():
#     # page = urlopen('https://www.python.org')
#     # print(page)
#     a = [i ** 2 for i in range(10000000)]
#     print(sum(a))
#
#
# func1()

# class Test:
#     @staticmethod
#     def func():
#         print('hello')
#
#     @classmethod
#     def func1(cls):
#         pass
#
#
# Test.func()
# import time
#
# Передача значений аргументов в декораторы
#
# def dec_func(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'Время выполнения функции {end - start}')
#         return result
#     return wrapper
#
#
# @dec_func
# def func1(n):
#     a = sum([i ** 2 for i in range(n)])
#     return a
#
#
# print(func1(5))

# Декораторы, которые принимают аргументы
import time


def func(i):
    # Декоратор
    def func_dec(func):
        def wrapper(*args, **kwargs):
            global result
            total = 0
            for j in range(i):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'общее время выполнения функции {total}')
            print(f'среднее время выполнения функции {total/i}')
            return result

        return wrapper

    return func_dec


@func(i=10)
def func1(n):
    a = sum([i ** 2 for i in range(n)])
    return a


print(func1(100000))
