# Домашнее задание по теме "строки и их методы"
# Реализовать приложение для проверки верности введенных пользователем данных в виде строки
# Проверим что пользователь ввел 3 слова и ФИО не содержит лишних символов

isCheck = True
while isCheck:
    name = input('Введите ФИО через пробел: ')
    if len(name.split()) == 3 and name.replace(' ', '').isalpha():
        print('Данные приняты\nФИО:', name)
        isCheck = False
    else:
        print('ФИО должносостоять из букв алфавита, и содержать Имя Фамилию и Отчество')


# Пример из лекции
pin = '1234'
while True:
    userPin = input('Введите пин код: ')
    if not userPin.isdigit() or len(userPin) != 4:
        print('Пинкод должен состоять из 4 цифр')
        continue

    if userPin == pin:
        print('Доступ подтвержден')
        break
    else:
        print('Вы ввели не правильный код')