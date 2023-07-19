# Реализовать программу использующую генераторы,
# и обрабатывающую данные последовательно с использованием итераторов

# Решение: Реализуем программу, которая ищет строки в тексте содержащие заданный текст,
# выводит найденные и считает их количество

# Пример 1: через функцию
def reader_iterator(file_name):
    for line in open(file_name, "r"):
        yield line


print('Поиск строк с текстом\n-----------------------------------------')
my_str = input('Введите искомый текст: ')
csv_gen = reader_iterator("text.csv")
row_count = 0
for row in csv_gen:
    # обработка данных
    str_to_list = row.split(';')
    if my_str in row:
        row_count += 1
        print(row)
print(f"Количество строк {row_count}")


# Пример 2: реализация генератора в классе
class StringSearch:
    def __init__(self, my_dir, char=''):
        self.count = 0
        self.my_dir = my_dir
        self.char = char
        self.file = open(my_dir, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if self.char in line:
                self.count += 1
                return line
        else:
            print(f'Количество строк: {self.count}')
            self.file.close()
            raise StopIteration


print('------------------------------------')
print('Поиск строк с текстом через класс\n-----------------------------------------')
my_str = input('Введите искомый текст: ')

my_iter = StringSearch('text.csv', my_str)
for row in my_iter:
    print(row)
