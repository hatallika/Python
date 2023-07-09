# Реализовать поиск последовательности Фиббоначи, А также найти элементы повторяющиеся в коллекции

# Найдем последовательность Фиббоначи из n элементов
n = 20
sequenceFib = []
for i in range(n):
    if i == 0 or i == 1:
        sequenceFib.append(i)
    else:
        sequenceFib.append(sequenceFib[i - 2] + sequenceFib[i - 1])
print(*sequenceFib)

# Найдем повторяющиеся элементы в коллекции
coll = [1, 4, 5, 7, 1, 3, 1, 4]

duplicates = set([])
# через количество
for i in coll:
    if coll.count(i) > 1:
        duplicates.add(i)
print(*duplicates)

# через словарь с подсчетом повторений
duplicates = {}
for item in coll:
    if item in duplicates:
        duplicates[item] += 1
    else:
        duplicates[item] = 1
for item, count in duplicates.items():
    if count > 1:
        print(f'Элемент {item} встречается {count} раз')

# через fromkeys
keys = set(coll)
# словарь элементов со значениями по умолчанию
rez = dict.fromkeys(keys, 0)

for key in coll:
    rez[key] += 1
for item, count in rez.items():
    if count > 1:
        print(f'Элемент {item} встречается {count} раз')
