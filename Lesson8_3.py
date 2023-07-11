# Функции продолжение. Методы
# def main12(x, y):
#     '''Эта функция возвращяет сумму переменных'''
#     return x + y

# print(main12(3,5))
# print(main12(3, 1))
# # print(main.__doc__)
# # print(dir(main))
# print(main12.__name__)
# print(main12.__module__)

# def main1(n, *args, **kwargs):
#     print(f'{n=}')
#     print(f'{args=}')
#     print(f'{kwargs=}')

# def main1(n, *args, **kwargs):
#     if args:
#         for ar in args:
#             n += ar
#     if kwargs:
#         for ar in kwargs.values():
#             n += ar
#     return n
#
# print(main1(2, 2, 3, 4, 5, x=2, y=1))
#
# main1(2, 3, 4, 5, x=5, y=7)
# if __name__ == '__main__':
#     print('Меня вызвали как основную функцию')
#     print(main12(3, 2, 4))
# else:
#     print('Меня импортировали как сторонний модуль')

# Рекурсия
# def recur(n):
#     if n == 0:
#         return 1
#     print(f'{n=}')
#     return recur(n - 1)
#
#
# recur(10)


# Бесконечная рекурсия
# import sys
#
# sys.setrecursionlimit(5000)
#
#
# def main(n):
#     print(f'{n=}')
#     return main(n + 1)

# def main(n):
#     if n <= 0:
#         return 1
#     return n * main(n - 1)
#
#
# print(main(5))

# def main(n):
#
#     while True:
#         if n > 10:
#             return
#         print(n)
#         n += 1
#
#
# main(2)

# num = int(input('Введите номер месяца '))


# def seasons(n):
#     match n:
#         case 1 | 2 | 12:
#             return 'Зима'
#         case 3 | 4 | 5:
#             return 'Весна'
#         case 6 | 7 | 8:
#             return 'Лето'
#         case 9 | 10 | 11:
#             return 'Осень'
#         case _:
#             return 'Error'
#
#
# result = seasons(num)
# print(result)

# def bank(summ, years):
#     for i in range(years):
#         summ += summ * 0.1
#         print(summ)
#     return summ
# print(bank(100, 3))
