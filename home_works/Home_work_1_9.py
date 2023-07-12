# Реализация приложения, которое считывает данные с файла, и сохраняет рассчитанное значение в файл
# на ПК пользователя

# Планируемый результат:#
# Реализовано приложение для обработки текстовой информации полученной с файла пользователя
# и сохраняющее результат в файловой системе ОС пользователя

# Расчитаем зарплату сотрудников от часов их работы

import csv

# Прочитаем данные сотрудников из файла
file = open('worktime.csv', encoding="utf8")
reader = csv.DictReader(file, delimiter=',')
worktime = []
# Вычислим зарплату
for line in reader:
    line['Зарплата'] = str(int(line['количество часов']) * int(line['сумма договора в час']))
    print(line)
    # Запишем вычисление в список
    worktime.append(line)
print(worktime)

# Запишем данные с расчетом зарплаты в новый файл
keys = worktime[0].keys()
with open('salary.csv', mode='w', encoding='utf-8') as newfile:
    writer = csv.DictWriter(newfile, keys)
    writer.writeheader()
    writer.writerows(worktime)

file.close()
# Прочитаем полученый файл и выведем зарплату сотрудников
with open('salary.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for employer in reader:
        print(employer['ФИО сотрудника'], employer['Зарплата'], sep=' | ')
