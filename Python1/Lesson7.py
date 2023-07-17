import random

# a = []
# print(type(a))
# b = list((1, 2, 3))
# print(type(b))
# c = list('hello')
# print(type(c))
# d = [1, 2, 3, 4]
# print(type(d))

# a = [1, 2, 3, ['a', 4], True, 'hello']
# a = [1, 2, 3]
# b = a
# b = a.copy()
# b.append(4)
# print(id(a))
# print(id(b))
# a = [1, 2, 3, 2]
# a.reverse()
# print(a)
# print(a.index(2))
# print(a.count(2))
# a.remove(2)
# print(a)
# b = a.pop(2)
# print(b)
# a.clear()
# print(a)

# idx = a.index(3)
# print(idx)
# b = [a[idx]]
# print(b)

# a = [1, 2, 3, 2]
# random.shuffle(a)
# print(a)
# a.sort()
# print(a)

# a = [1, 2, 3, 2]
# a.insert(1, [1, 2, 3])
# print(a)
# b = [[4, 5, 6]]
# a.extend(b)
# print(a)

# a = [1, 2, 3, 4, 5, 6, 1, 3]
# b = [2, 5, 8, 7, 6]
# c = []
# for num in a:
#     if num not in b and num not in c:
#         c.append(num)
# print(*c)
#
# for num in set(a):
#     if num not in b:
#         print(num)

# a = ['a', 'b', 'c', 'd', 'a']
# b = set(a)
# print(b)
# b = list(b)
# print(b)
# a = ()
# a = (1, )
# a = 1, 2
# a = tuple([1, 2])
# a = tuple('hello')
# print(a)
# print(type(a))
# print(a[::-1])
# print(a[::-2])

# a = 6
# b = 5
# a, b = b, a
# print(a, b)

# a, b, c = 1, 2, [1, 2, 3]
# print(a, b, c)

a = (1, 2)
b, c = a
print(b, c, sep='| ')