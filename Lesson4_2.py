# word = 'pencil table pen'
# if 'pen' in word:
#     print('YES')

# language = []
# while True:
#     lang = input('Введите язык програмирования: ')
#     if lang not in language:
#         language.append(lang)
#     print(language)

# language = ['Python', 'C#']
# while True:
#     lang = input('Введите язык программирования: ')
#     if lang in language:
#         print(f'Я  знаю {lang}')
#     else:
#         print(f'Я не знаю {lang}')
#     if lang not in language:
#         language.append(lang)
#     else:
#         print('Данный язык уже есть')
#     if input('Для выхода нажмите 0. Ввод для продолжения: ') == '0':
#         break

# print('Вклад в банк')
# account = int(input('Введите сумму: '))
# years = int(input('Введите срок: '))
# for i in range(years):
#     account += account * 0.1
# print(account)

# print(5 < 3)
# print(2 > 1)

# a = [1, 2, 3, 4, 5]
# for num in a:
#     if num % 2 != 0:
#         continue
#     print(num)

# a = [1, 2, 3, 4, 5, 6]
# n = len(a)
# i = 0
# while i < n:
#     if a[i] % 2 == 0:
#         a[i] = a[i] // 2
#         i += 1
#     else:
#         a.remove(a[i])
#         n -= 1
# print(a)

# while True:
#     number = int(input('Введите номер места: '))
#     if 0 < number <= 36:
#         # if number % 4 == 0:
#         #     print(number // 4)
#         # else:
#         #     print(number // 4 + 1)
#         print(-(-number // 4))
#     else:
#         print('Неверный номер места')

# Синтаксический сахар
# a = [i for i in range(1, 101) if i % 3 == 0]
# print(a)

# Тернарный оператор
number = 5
x = 'Четное' if number % 2 == 0 else 'Нечетное'
print(x)
