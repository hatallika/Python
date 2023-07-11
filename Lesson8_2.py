# Функции, Анонимные Функции, Исключения
# Рекурсии
# def fact(n):
#     if n == 1:
#         return 1
#
#     return n * fact(n - 1)

# абстрактное разложение
# def fact(3):
#     if 3 == 1:
#         return 3
#     return  3 * fact(3-1)
#
# def fact(2):
#     if 2 == 1:
#         return 3
#     return  3 * fact(2-1)
#
# def fact(1):
#     if 1 == 1:
#         return 3
#     return  3 * fact(1-1)
#
# print(fact(3))

# x = lambda: 'welcome'
# y = lambda x: print(f'world {x()}')
#
# y(x)

# def main(func):
#     print('hello')
#     func()
#     print('end')
#
#
# func  = lambda: print('world')
#
# main(func)
import tkinter.messagebox as tmb


def main():
    print('Выберите действие')
    work_list = []
    while True:
        choice = input('1 - Добавить; 2 - Изменить; 3 - Удалить; 4 - Вывести все; 0 - Выход\n')

        match choice:
            case '1':
                add_db(work_list)
            case '2':
                change_db(work_list)
            case '3':
                del_db(work_list)
            case '4':
                print_all(work_list)
            case '0':
                break
            case _:
                print('Неправильный выбор')


def add_db(work):
    number = int(input('Введите значение для добавления: '))
    if number not in work:
        work.append(number)
        print(work)
    else:
        print('Данное значение уже есть')


def change_db(work):
    number = int(input('Введите значение для изменения: '))
    # if number in work:
    try:
        idx = work.index(number)
        number = int(input('Введите новое значение: '))
        work[idx] = number
        print(work)
    # else:
    except Exception as err:
        print('Нет такого значения в списке')
        print(err)


def del_db(work):
    number = int(input('Введите значение для удаления: '))
    try:
        work.remove(number)
        print(work)
    except Exception as err:
        print('Нет такого значения в списке')
        print(err)


def print_all(work):
    print(work)


if __name__ == '__main__':
    main()
