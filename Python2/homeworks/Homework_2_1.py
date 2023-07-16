# Домашнее задание
# Создание собственных модулей на языке Python
# Реализация модуля для импорта и дальнейшего использования в приложении
# Решение: создадим модуль с разной сортировкой списков в mymodule.py

from mymodule import bubble_sort, selection_sort, heap_sort

my_list = [7, 10, 2, 5, 1, 3]
# Пузырьковая сортировка
bubble_sort(my_list)
print(my_list)

my_list2 = [7, 10, 2, 5, 1, 3]
# Сортировка выбором
selection_sort(my_list2)
print(my_list2)

my_list3 = [35, 12, 43, 8, 51]
# Сортировка куча
heap_sort(my_list3)
print(my_list3)
