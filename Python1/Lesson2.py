import random

secret_number = random.randint(1, 10)
attempts = 3
print('Угадай число от 1 до 10')
while attempts > 0:
    user_number = int(input('Введите число от 1 до 10: '))
    if user_number == secret_number:
        print('Вы угадали')
        break
    elif user_number < secret_number:
        print('Секретное число больше')
    elif user_number > secret_number:
        print('Секретное число меньше')
    attempts -= 1
    if attempts == 0:
        # print('Вы проиграли. Секретное число:  ' + str(secret_number))
        print(f'Вы проиграли. Секретное число: {secret_number}')
