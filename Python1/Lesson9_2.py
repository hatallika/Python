import csv
# with open('text/test.csv', mode='r') as file:
#     # print(file.read())
#     reader = csv.reader(file, delimiter=';')
#     for line in reader:
#         print(line)

# with open('text/test.csv', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     print(type(reader))
#     for line in reader:
#         print(line.keys())

# file = open('text/test.csv', encoding='windows-1251')
# reader = csv.DictReader(file, delimiter=';')
#
# print(reader.fieldnames)
# columns = reader.fieldnames
# запись в csv файл
# with open('text/test2.csv', mode='w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(reader)
# file.close()

print('Блокнот\n________________________')
mode = 'r'
file_name = input('Введите название файла (существующего): ')
# Прочитать из файла и записать в список
word_text = open(f'text/{file_name}.txt', mode=mode)
words_rows = word_text.readlines()
print(words_rows)
while True:
    mode = 'w'
    choice = input('Введите пункт меню: 1. Добавить, 2. Перезаписать файл, 3. Очистить, 0 - Вывести все и выйти\n')
    match choice:
        case '1':
            print('-- Добавление в файл --')
            new_str = input('Введите новую строку: ')
            new_str = '\n' + new_str
            words_rows.append(new_str)
            mode = 'a'
        case '2':
            print('-- Перезапись в файл --')
            words_rows = []
            new_str = input('Введите строку для перезаписи')
            words_rows.append(new_str)
            mode = 'w'
        case '3':
            words_rows = []
        case '0':
            with open(f'text/{file_name}.txt', mode=mode) as file:
                if words_rows:
                    print(words_rows[-1])
                    file.writelines(words_rows[-1])
        case _:
            print('Error')
