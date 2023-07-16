# Set Множества
# a = {}  # dict
# a = set([])
# a = {1, 2, 3, 1}
# print(type(a))
# a = set(a)
# a = list(set(a))
# print(a)
# a = {1, 2, 3, 4, 5, 6}
# b = {4, 5, 6}
# c = {'a', 'b', 'c'}
# a.update([4, 5])
# c.pop()
# print(a)
# print(c)
# a.remove(3)
# a.add(4)
# a = {1, 2, 3, (1, 2, 3)}
# print(a.union(b, c))
# print(a.difference(b))
# a.difference_update(b)
# print(a)
# print(a.intersection(b))
# print(a)
# a.intersection_update(b)
# print(a)
# print(a.symmetric_difference(b))
# print(a.isdisjoint(b))
# if a.isdisjoint(b):
#     print('No')
# else:
#     print('Yes')
# print(a.issubset(b))
# c = [1, 2, 3]
# d = [3, 2, 1]
# print(set(c) == set(d))
# print(a.issuperset(b))
# a = frozenset([1, 2, 3, 4, 1])
# a = set(a)
# print(a)
# найти общие элементы в списках, итог уникальные элементы.
# a = [1, 2, 3, 4, 1]
# b = [1, 2, 5]
# c = []
# через цикл
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#         # print(i, end=" ")
# print(*c)
# # через множества
# print(set(a).intersection(set(b)))

# a = {1, 2, 3}
# for i in a:
#     print(i)

a = {'a': 1, 'b': 2, 'c': 3}
# for i in a:
#     print(i)
# for i in a.keys():
#     print(i)
# for i in a.values():
#         print(i)
for k, v in a.items():
    print(f'Ключ {k}: значение  {v} ')
