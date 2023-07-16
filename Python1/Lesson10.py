# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print('метод __new__')
#     def __init__(self, name, age):
#         print('метод __init__')
#         self.name = name
#         self.age = age
#
#     # name = 'Иван'
#     # age = 37
#
#     def say_hello(self):
#         print(f'Hello, {self.name}')


# person1 = Person()
# person2 = Person()
# person1.say_hello()
# print(type(person1))
# print(person1.name)
# print(person1.age)
# person1.say_hello()

# person1.name = 'Федор'
# Person.name = 'Федор'
# print(person1.name)
# print(person2.name)
# person1 = Person('Иван', 27)
# person2 = Person('Федор', 24)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)

# class Car:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     def say_color(self):
#         return f'Цвет = {self.color}'
#
#     def say_speed(self):
#         print(f'Скорость = {self.speed}')
#
#
# car1 = Car('black', 100)
# car2 = Car('white', 110)
#
# print(car1.color)
# car1.color = 'yellow'
# print(car1.color)
# print(car1.say_color())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Привет! Меня зовут {self.name}'


class Person1(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


person1 = Person1('Иван', 27)
person2 = Person1('Федор', 40)
print(person1.name)

print(person1.say_hello())
print(person2.say_hello())