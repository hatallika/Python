# Модуль 2: Урок 2: Генераторы и Итераторы
# for i in range(1, 10):
#     print(i)

# Генераторы
# def func(args):
#     while True:
#         yield args
#         args += 1
#
#
# for i in func(5):
#     if i == 10:
#         break
#     print(i)
#
#
# result = func(5)
# print(next(result))

# num_list = [1, 2, 3, 4, 5]
# elem = iter(num_list)
# for i in elem:
#     print(i)
#
#
# print(next(elem))
# print(next(elem))
# print('Hello')
# print(next(elem))

# for i in num_list:
#     print(i)

# def next_cube():
#     acc = 1
#     while True:
#         yield acc ** 3
#         acc += 1  # После след обращения исполнение продолжится отсюда
#
#
# count = 1
# for num in next_cube():
#     if count > 15:
#         break
#     print(num)
#     count += 1

# class MyIterator:
#     def __init__(self, val):
#         self.val = val
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.val:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# my_iter = MyIterator(5)
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# for i in my_iter:
#     print(i)

# def func():
#     yield 'Python'
#     yield 'C#'
#     yield 'C++'
#     yield 'Java'
#
#
# x = func()
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
#
# for i in x:
#     print(i)

# def func(number):
#     for item in range(1, 11):
#         yield item * number
#
#
# result = func(10)
# for i in result:
#     print(i)
import time


class Fib:
    def __init__(self):
        self.prev = 0
        self.cur = 1
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 10000:
            result = self.prev + self.cur
            self.prev = self.cur
            self.cur = result
            self.n += 1
            return result
        else:
            raise StopIteration


start_iter = time.time()
iterator = iter(Fib())
# for i in iterator:
#     print(i)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print('Итерация окончена')
        break
end_iter = time.time()

start = time.time()
# Программа повисла
fib = [0, 1]
counter = 0
while len(fib) < 10000:
    fib.append(fib[counter] + fib[counter + 1])
    counter += 1
print(fib)
end = time.time()
time1 = end_iter - start_iter
time2 = end - start
print(f' Класс {time1}')
# print(f'Конец класса {end_iter}')
print(f'Начало  {time2}')
# print(f'Конец  {end}')
