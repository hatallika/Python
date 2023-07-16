# while
# count = 10
# while count > 0:
#     print(count)
#     count -= 2

# бесконечный цикл
# while True:
#     print('Hello')

# Выводить только четные цифры
# count = 10
# while count > 0:
#     if count % 2 == 0:
#         print(count)
#     count -= 1

# Выход из цикла
# count = 0
# while True:
#     count += 1
#     print(count)
#     if input('Для выхода нажмите 0: ') == '0': #Выход действием пользователя
#         print('Цикл завершен')
#         break
# print(count)

# count = 0
# while 1:
#     count += 1
#     if count == 10: #Выход из цикла по условию
#         break
# print(count)

# range функция
# x = range(1, 10, 2)
# print(type(x))
# print(x.start)
# print(x.stop)
# print(x.step)

# Переберем четные числа и составим из них строку
# string1 = ''
# count = 1
# while True:
#     if count % 2 != 0:
#         string1 += str(count)
#
#     count += 1
#     if count >= 12:
#         break
# print(string1)

# Задача спросить пользователя его данные, и выйти в зависимости от ответа

people = []
while True:
    choice = input('1 - Добавить, 2 - Удалить, 3-Изменить, 4-Вывести все, 0 - Выход:\n')
    match choice:
        case '1':
            people.append(input('Введите имя: '))
        case '2':
            userName = input('Введите имя для удаления из списка: ')
            if userName in people:
                people.remove(userName)
            else:
                print('Такого имени нет в списке')
        case '3':
            userName = input('Введите имя для изменения: ')
            if userName in people:
                idx = people.index(userName)
                newName = input('Введите новое имя: ')
                people[idx] = newName
        case '4':
            # print(*people)
            # for item in people:
            #     print(item)
            i = 0
            while i < len(people):
                print(f'{i + 1}. {people[i]}')
                i += 1
        case '0':
            print('Программа завершена')
            break
        case _:
            print('Нет такого пункта меню')