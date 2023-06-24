# Реализовать программу, показывающую различные подходы к использованию разных типов данных
# string, boolean
isValidName = False
while not isValidName:
    firstName = input('Введите ваше имя: ')
    if firstName.isalpha():
        print('Hello, ' + firstName.title())  # конкатенация
        print(f'Ваше имя состоит из {len(firstName)} букв')  # f-строка
        isValidName = True
    else:
        print("Имя может состоять только из букв алфавита")

# integer - операции с числами
print('Введите два числа')
a, b = int(input()), int(input())
print(f'Число {a} в степени {b} =', a ** b)
print(f'Произведение {a} * {b} =', a * b)
print(f'Сумма {a} + {b} =', a + b)
print(f'Разница {a} - {b} =', a - b)
if a > b:
    remainder = a % b
else:
    remainder = b % a
print('Остаток от деления большего числа на меньшее: ', remainder)
if b != 0:
    print('Деление', a / b)

# list
name = input('Введите ФИО в одну строку: ')
list = name.split()
print(f'Фамилия с инициалами: {list[0]} {list[1][:1]}. {list[2][:1]}.')  # Используем срез для сокращения инициалов

# Список покупок
shopping_list = []
print('Составим список покупок.\nВведите товары по одному, чтобы закончить ввод введите "stop" или "-"')
while True:
    product = input()
    if product == 'stop' or product == '-':
        break
    else:
        shopping_list.append(product)
print('Список покупок:')
for idx, item in enumerate(shopping_list):
    print(str(idx + 1) + ". ", item)
while len(shopping_list) > 0:
    num = int(input('Какой товар удалить из списка? Укажите номер: '));
    shopping_list.pop(num-1)
    for idx, item in enumerate(shopping_list):
        print(str(idx + 1) + ". ", item)


# Задача из лекции. Угадываем слово по буквам
print('Угадай слово по буквам')
secret_word = 'apple'
for char in range(len(secret_word)):
    print('*', end=' ')
print()
user_chars = []
attempts = 3
while attempts > 0:
    isWin = True
    user_char = input('Введите букву: ')
    user_chars.append(user_char)
    for char in secret_word:
        if user_char == char or char in user_chars:
            print(char, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()
    if user_char not in secret_word:
        attempts -= 1
    if attempts == 0:
        print('Вы проиграли')
        print(f'Секретное слово {secret_word}')
    if isWin:
        print('Вы угадали все слово')
        break

# Преобразование списка в множество и в словарь
# list to set
list2 = [1, 2, 4, 5, 6]
print(set(list2))
# list to dict
item = [('модель', 'Lada'), ('цвет', 'черный'), ('количество', 7)]
item_dict = dict(item)
print(item_dict)

