# Переменные и условия
# number = 2
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# age = 35
# if age == 35:
#     print('Вам 35 лет')
# elif age < 35:
#     print('Вам меньше 35 лет')
# if age > 35:
#     print('Вам меньше 35 лет')
# if age >= 35:
#     print('Вам 35 лет или больше')
# elif age <= 35:
#     print('Вам 35 лет или меньше')
# if age != 35:
#     print('Вам не 35 лет')

# if 5 == "5":
#     print('Равны')
# else:
#     print('Не равны')

# flag = True
# while flag:
#     print('1 - Добавить\n2 - Изменить\n3 - Удалить')
#     choice = input('Введите число:')
#     if choice == '1':
#         print('Добавить')
#         flag = False
#     elif choice == '2':
#         print('Изменить')
#         flag = False
#     elif choice == '3':
#         print('Удалить')
#         flag = False
#     else:
#         print('Вы ошиблись. Такого пункта нет')

# print('1 - Добавить\n2 - Изменить\n3 - Удалить')
# choice = input('Введите число:')
# match choice:
#     case '1' | '2' | '3':
#         print('YES')
#     case _:
#         print('Вы ошиблись')

# number = 3
# if 1 < number < 5:
#     print('YES')

# money = True
# product = False
# if money is True and product is True:
#     print('Вы можете купить')
# else:
#     print('ERROR')
#
# x = 5
# a = 5

# money = False
# product = False
# if money is True or product is True:
#     print('YES')
# else:
#     print('NO')

# season = ''
# num = int(input('Введите номер месяца '))
# if num == 12 or 0 < num <= 2:
#     season = 'Зима'
# elif 2 <= num <= 5:
#     print('Весна')
# elif 6 <= num <= 8:
#     print('Лето')
# elif 9 <= num <= 11:
#     print('Осень')
# print(season)

# match num:
#     case 1 | 2 | 12:
#         season = 'Зима'
#     case 3 | 4 | 5:
#         season = 'Весна'
#     case 6 | 7 | 8:
#         season = 'Лето'
#     case 9 | 10 | 11:
#         season = 'Осень'
#     case _:
#         print('Ошибка')
# print(season)
number = 3
if number > 1:
    if number < 5:
        print('YES')
