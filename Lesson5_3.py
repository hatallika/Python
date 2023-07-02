# Циклы часть 3
# Игра крестики нолики
game_round = 1
while True:
    print()
    choice = input('Хотите начать игру?(да/нет): ').lower()
    if choice == 'нет':
        break
    elif choice == 'да':
        print(f'Раунд {game_round}')
        game_round += 1
        print()
        print('Добро пожаловать в игру крестики нолики')
        print()

        area = []
        for i in range(3):
            area.append([])
            for j in range(3):
                area[i].append('*')
        for _ in area:
            print(_)
        step = 1
        while True:
            char = 'O' if step % 2 == 0 else 'X'
            print(f'Ходит {char}')

            row = int(input('Введите строку: '))
            column = int(input('Введите столбец: '))

            if area[row - 1][column - 1] == '*':
                area[row - 1][column - 1] = char
            else:
                print('Клетка уже занята')
                continue
            step += 1

            if area[0][0] == area[0][1] == area[0][2] == 'X':
                print('Победили крестики')
                break
            if area[0][0] == area[0][1] == area[0][2] == 'O':
                print('Победили нолики')
                break
            if step == 10:
                print('Ничья')
                break

            for _ in area:
                print(_)
        for _ in area:
            print(_)
    else:
        print('Вы сделали не правильный выбор')