# 1_6 Строки и их методы
# word = 'hello'
# for char in word:
#     print(char)
# print(word[1])
# print(len(word))
# word1 = word[:4]
# print(word[1::2])
# word1 = word[3:] + 'wer'
# print(word1)
# print(word[-1])
# print(word[::-1])

# word = input()
# if word == word[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')
# word = input()
# print(word.ljust(10, '.'))
# print(word.rjust(10, '.'))
# print(word.isdigit())
# pin = '1111'

# while True:
#     userPin = input('Введите пин код: ')
#     if not userPin.isdigit() or len(userPin) != 4:
#         print('Пинкод должен состоять из 4 цифр')
#         continue
#
#     if userPin == pin:
#         print('Доступ подтвержден')
#         break
#     else:
#         print('Вы ввели не правильный код')

# word = 'hello world'
# print(word.istitle())
# print(word.title())
# print(word.capitalize())
# print(word.isalpha())
# print(word.count('ll'))
# print(word.index('ll'))
# print(word.endswith('lo'))
# print(word.startswith('he'))
# print(word[len(word) - 1])
#
# secret_word = input()
# if secret_word.startswith('start') and secret_word.isalpha() and secret_word.endswith('word'):
#     print('Все верно')

# print('hello'.upper())
# print('HELLO'.lower())
# print('HELLO'.casefold())
# print('helLo'.islower())
# print('helLo'.isupper())
# print('hello1.'.isalnum())
# print('hello'.split())
# print('hello world'.split())
# print('hello world, hello world, hello world, hello world'.split(sep=',', maxsplit=2))

# nums = []
# for i in range(3):
#     nums.append(input())
# print(nums)
#
# nums = input().upper().split()
# print(nums)

# name = 'Ruslan'
# print('Привет {}'.format(name))
# print(name * 2)

print('hello'.center(11, '.'))