# def hello():
#     print('hello world')
#
#
# hello()

# side = int(input('Введите сторону квадрата: '))
# area = side * side
# print(area)

# mySide = int(input('Введите сторону квадрата: '))

# area = 0
#
# def main(side):
#     global area
#     area = side * side
#     print('Внутри функции')
#     print(area)
#
#
# print('Вне функции')
# print(area)
#
# main(5)
# def main1():
#     area = 5
#     print(id(area))
# print('Вне функции')
# print(area)

# main(mySide)
# main1()
# area = main(mySide)
# print(area)

# def main():
#     return 5 * 4, 5


# print(main())
# result, number = main()
# print(result, number)

# def fact(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# print(fact(5))

# x = 0
#
#
# def main():
#     # global x
#     x = 1
#     print(f'Внутри main {x=}')
#
#     def sub_main():
#         nonlocal x
#         x = 2
#         print(f'Внутри sub_main {x=}')
#
#     sub_main()
#     print(f'Внутри main после вызова sub_main {x=}')
#
#
# print(x)
# main()
# print(x)

# print(lambda: 1 + 1)
#
# summ = lambda: 1 + 1
# print(summ())

# summ = lambda : True
# print(summ())

# print((lambda x: x ** 2)(3))
# summ = lambda x: x + x
# print(summ(5))
# summ = lambda x, y: x + y
# print(summ(2, 4))

def my_perimeter(side1, side2 = 0):
    return (side1 + side2) * 2


print(my_perimeter(2))
