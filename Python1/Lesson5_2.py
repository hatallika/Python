# Цикл for
# for i in range(1, 10, 2):
#     # pass заглушка для тела цикла
#     print('hello')

# word = 'hello world'
# for char in word:
#     print(char, end=' ')

# for i in range(len(word)):
#     print(word[i])

# a = ['a', 'b', True, 1]
# for i in range(len(a)):
#     a[i] = 1
# print(a)

# перебор с индексом
# for i, elem in enumerate(a):
#     print(i + 1, elem, sep='.')
#
# for i in range(len(a)):
#     print(f'{i + 1}.{a[i]}')

# Переберем список до определенного элемента, который сохраним в список для дальнейшего взаимодействия
# number = 247
# list_number = [1, 2, 3, 5, 247, 10, 2]
# for _ in list_number:
#     print(_)
#     if _ == number:
#         break

# while else
# count = 0
# while count < 5:
#     print('Цикл выполняется')
#     count += 1
# else:
#     print('Цикл завершился')

# fib = [0, 1]
# count = 0
# n = len(fib)
# for i in range(len(fib)):
#     fib.append(1)
#     print(fib)
#     n += 1
# while fib[len(fib)] < 100:
# while fib[-1] < 100:
#     fib.append(fib[count] + fib[count + 1])
#     count += 1
# fib_len = len(fib)
# print(fib[:fib_len - 1])
# while len(fib) <= 100:
#     fib.append(fib[-2]+fib[-1])
# print(fib)

# while len(fib) <= 100:
#     fib.append(fib[count] + fib[count+1])
#     count += 1
# print(fib)

# Добавление чисел кратных 3 в список
# list_numbers = []
# for i in range(50, 100):
#     if i % 3 == 0:
#         list_numbers.append(i)
#     if len(list_numbers) == 5:
#         break
# print(list_numbers)

# Вложенные циклы
# for i in range(3):
#     for j in range(3):
#         print(i, j, sep=':')
# Пример наполнения списка вложенными циклами
a = []
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append('*')
# print(a)
for i in range(len(a)):
    print(a[i])
