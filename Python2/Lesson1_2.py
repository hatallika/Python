# import os
# from dotenv import load_dotenv
# load_dotenv()
# password = os.getenv('PASSWORD')
# username = os.getenv('USER_NAME')
# print(password, username)
# from mymodule.mymodule import *
from mymodule.mymodule import operations, PI
print(PI)
print(' -- Калькулятор --')
while True:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    action = input('-- Введите действие --\n+ - Сложение\t- - Вычитание\n/ - Деление\t* - Умножение\n\t\t0 - Выйти\n')
    match action:
        # case '1':
        #     print(add_number(num1, num2))
        # case '2':
        #     print(sub_number(num1, num2))
        # case '3':
        #     print(div_number(num1, num2))
        # case '4':
        #     print(mul_number(num1, num2))
        case '+':
            print(operations(num1, num2, action))
        case '-':
            print(operations(num1, num2, action))
        case '/':
            print(operations(num1, num2, action))
        case '*':
            print(operations(num1, num2, action))
        case '0':
            break
        case _:
            print('Нет такого пункта меню')

print('Программа завершена')
