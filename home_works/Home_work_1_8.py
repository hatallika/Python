# Реализация программы используя прошлый материал для нахождения результата, согласно условиям задачи
# Реализовать текущую задачу с использованием функций

# Найдем последовательность Фиббоначи из n элементов

def fibonacci_sequence(n):
    sequence_fib = []
    for i in range(n):
        if i == 0 or i == 1:
            sequence_fib.append(i)
        else:
            sequence_fib.append(sequence_fib[i - 2] + sequence_fib[i - 1])
    return sequence_fib


print(fibonacci_sequence(20))


# Через рекурсию, найти номер последовательности
# n - номер числа последовательности: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
def rec_fibb(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return rec_fibb(n - 2) + rec_fibb(n - 1)


for i in range(1, 21):
    print(rec_fibb(i), end=' ')
print()

# Найдем повторяющиеся элементы в коллекции
coll = [1, 4, 5, 7, 1, 3, 1, 4, 4]


def get_duplicates(mylist):
    duplicates = set([])
    for item in mylist:

        if mylist.count(item) > 1:
            duplicates.add(item)
    return duplicates


print('Повторяются:', *get_duplicates(coll))
