# List comprehension

# # List comprehension с изменением
# nums = [n * n for n in range(1, 6)]
# print(nums)
#
# # List comprehension с if
# nums = [1, 2, 3, 4, 5]
# odd_squares = [n * n for n in nums if n % 2 == 1]
# print(odd_squares)
#
# # List comprehension с вложенным циклом for
# matrix = [
#     [x for x in range(1, 4)]
#     for y in range(1, 3)
# ]
# print(matrix)
#
# # Cписок дней рождения из списка словарей
# people = [
#     {
#         "first_name": "Василий",
#         "last_name": "Марков",
#         "birthday": "9/25/1984"
#     },
#     {
#         "first_name": "Регина",
#         "last_name": "Павленко",
#         "birthday": "8/21/1995"
#     }
# ]
# birthdays = [
#     person[term]
#     for person in people
#     for term in person
#     if term == "birthday"
# ]
# print(birthdays)

# my_list = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)

# my_list = [i for i in range(1, 10) if i % 2 == 0]
# my_list = [str(i) for i in range(1, 10) if i % 2 == 0]
# my_list = [i ** 2 for i in range(1, 10) ]
# print(my_list)

# chars = [i for i in 'hello']
# print(chars)

# my_list = [i for i in range(1, 10) if i % 2 == 0]
# print(my_list)

# my_list = [[i * j for i in range(1, 4)] for j in range(1, 4)]
# print(my_list)

# my_list = [[0 for i in range(2)] for j in range(3)]
# for i in my_list:
#     print(i)
# print(my_list)
# print((lambda x: x + 2)(2))

# my_list = [(lambda i: i * i)(i) for i in range(0, 10)]
# print(my_list)
# import itertools
#
# my_list = [i for i in itertools.repeat('hello', 5)]
# print(my_list)

# my_tuple = (i for i in range(1, 5))
# print(my_tuple)  # <generator object <genexpr> at 0x000002635C5F8040>
# print(next(my_tuple))
# print(next(my_tuple))
# print(next(my_tuple))
#
# # Генерация кортежей
# my_tuple = tuple([i for i in range(1, 5)])
# print(my_tuple)
#
# my_set = { i for i in range(1, 5)}
# print(my_set)

# генератор словарей (dict)
# my_dict = {x: x ** 2 for x in range(1, 10) if x % 2 == 0}
# print(my_dict)

# my_dict = {x: y for x in 'abc' for y in 'def'}
# print(my_dict)

# my_dict = {x: 0 for x in range(1, 10)}
# my_dict = {x: 0 for x in [1, 3, 5, 7]}
# print(my_dict)

# генерация словаря с помощью fromkeys
# my_dict = {}.fromkeys('abc', 0)
# print(my_dict)
# # {'a': 0, 'b': 0, 'c': 0}
# my_dict = {}.fromkeys(range(1, 10), 0)
# print(my_dict)
# # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

# генерация распаковкой в кортежи
# my_dict = list(zip('abc', range(3)))
# print(my_dict)
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)

# print(list(zipped_values))
# my_list = list(zip('abc', range(3)))
# my_dict = {x: y for x, y in my_list}
# print(my_dict)

# my_dict = {x: [y for y in range(x, x + 3)] for x in range(4)}
# print(my_dict)

# my_dict = { x: {y for y in 'xyz'} for x in 'abc'}
# print(my_dict)

# my_dict = dict(zip('abcd', range(4, 8)))
# print(my_dict)
import math

num = int(input('Введите число: '))
result = [math.sqrt(i) for i in range(1, num)]
print(result)
result = [i ** 0.5 for i in range(1, num)]
print(result)