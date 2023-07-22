# Декораторы(2) Цепочка декораторов

# def dec1(func):
#     def wrapper():
#         return f'____{func()}____'
#
#     return wrapper
#
#
# def dec2(func):
#     def wrapper():
#         return f'++++{func()}++++'
#
#     return wrapper
#
#
# @dec1
# @dec2
# def hello():
#     return 'hello'
#
#
# print(hello())

# def dec1(func):
#     def wrapper():
#         f = func()
#         list_f = f.split()
#         return list_f
#
#     return wrapper
#
#
# def dec2(func):
#     def wrapper():
#         f = func()
#         letter_upper = f.upper()
#         return letter_upper
#
#     return wrapper
#
#
# @dec1
# @dec2
# def func1():
#     return 'hello world python'
#
#
# print(func1())
# # ['HELLO', 'WORLD', 'PYTHON']

# Обрабтка исключений с помощью декоратора

# my_list = ['a', 'b', 'c']
#
#
# def dec1(func):
#     def newvalueof(pos):
#         if pos >= len(my_list):
#             print('Ошибка')
#             return
#         func(pos)
#
#     return newvalueof
#
# @dec1
# def valueof(index):
#     print(my_list[index])
#
#
# valueof()

# декораторы экземпляров класса
# import random
# from collections import deque
#
#
# class Test:
#     def __init__(self, cache_size=100):
#         self.cache_size = cache_size
#         self.call_args_queue = deque()
#         self.call_args_to_result = {}
#
#     def __call__(self, fn):
#         def new_func(*args, **kwargs):
#             mem_key = self._convert_call_argument_to_hash(args, kwargs)
#             if mem_key not in self.call_args_to_result:
#                 result = fn(*args, **kwargs)
#                 self.update_cache_key_with_value(mem_key, result)
#                 self._evict_cache_if_necessary()
#             return self.call_args_to_result[mem_key]
#
#         return new_func
#
#     def update_cache_key_with_value(self, key, value):
#         self.call_args_to_result[key] = value
#         self.call_args_queue.append(key)
#
#     def _evict_cache_if_necessary(self):
#         if len(self.call_args_queue) > self.cache_size:
#             oldest_key = self.call_args_queue.popleft()
#             del self.call_args_to_result[oldest_key]
#
#     @staticmethod
#     def _convert_call_argument_to_hash(*args, **kwargs):
#         return hash(str(args) + str(kwargs))
#
#
# @Test(cache_size=100)
# def func(max_value):
#     return random.random() * max_value
#
#
# print(func(10))

class Decorator:
    def __init__(self, func):
        print('Класс декратор __init__')
        self.func = func

    def __call__(self):
        print(f'Перед вызовом {self.func.__name__}')
        self.func()
        print('После вызова')


@Decorator
def func1():
    print('hello world')


print('Старт')
func1()
print('Конец')
# Класс декратор __init__
# Старт
# Перед вызовом func1
# hello world
# После вызова
# hello world
# Конец
