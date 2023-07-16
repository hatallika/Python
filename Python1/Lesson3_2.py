# print('welcome'.istitle())
# print('welcome'.title())

# city = 'Moscow'
# for i in range(len(city)):
#     print(city[i], end=' ')
# print()
# print('hello')

# list_number = [1, 2, 3, 4, 5, 6]
# for number in list_number:
#     if number%2 == 0:
#         print(number)

# gess word
print('Угадай слово по буквам!')
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
