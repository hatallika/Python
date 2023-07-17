# Файлы
# Чтение файла
# file = open('text/test.txt', 'r')
# result = file.read()
# result = file.readline()
# result = file.readlines()
# print(result)
# file.close()

# Чтение файла
# with open('text/test.txt', 'r') as file:
#     result = file.read()
# print(result)

# Запись файла
# file = open('text/test.txt', 'w')
# text = 'python'
# file.write(text)
# print(file.writable())
# file.close()
#
# file = open(file='text/test.txt', mode='w')
# text = input('Введите текст: ' )
# file.write(text)
# file.close()
#
# file = open('text/newtest.txt', 'w')
# file.write('hello world')
# file.close()
#
# file = open('text/newtest.txt', 'a')
# file.write('\npython language')
# file.close()
#
# file = open('text/newtest.txt', 'r')
# result = file.readlines()

# result_temp = result[0]
# idx = result_temp.find('\n')
# result_temp = result_temp.replace('\n', '')
# result_temp = result_temp.rstrip('\n')
# result[0] = result_temp
# result[0] = result_temp[:idx]
# result[0] = result[0].split(' ')
# print(result[0][1])

# file.close()
# file.writelines(result)

with open('../text/newtest.txt', 'w') as file:
    file.write('hello')
with open('../text/newtest.txt', 'a') as file:
    file.write('\nworld')
# with open('text/newtest.txt') as file:
#     print(file.read())
with open('Lesson9.py') as file:
    print(file.read())