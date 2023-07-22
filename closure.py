# Замыкание
# Функция outer определяется с функцией inner внутри, а функция outer возвращает функцию inner;
# именно она – возвращаемое значение outer.

# def outer():
#     x = 1
#
#     # Замыкание
#     def inner():
#         print(f' x in outer function: {x}')
#
#     return inner


# print(outer())
# <function outer.<locals>.inner at 0x0000026DCAC24680>
# outer()()
# x in outer function: 1
# f = outer()
# f()
# x in outer function: 1

# def outer():
#     x = 1
#
#     def inner():
#         nonlocal x
#         print(f'x in outer function (before modifying): {x}')
#         x += 1
#         print(f'x in outer function (after modifying): {x}')
#
#     return inner
#
#
# f = outer()
# # f()
# for i in range(5):
#     print(f'Run {i + 1}')
#     f()
#     print('\n')

# Фибоначи замыканием

# def fib():
#     x1 = 0
#     x2 = 1
#
#     def get_next_number():
#         nonlocal x1, x2
#         x3 = x1 + x2
#         x1, x2 = x2, x3
#         return x3
#         # x0, x1 = x1, x0 + x1
#         # return x1
#
#     return get_next_number
#
#
# fibonacci = fib()
# for i in range(2, 21):
#     num = fibonacci()
#     print(f'The {i}th Fibonacci number is {num}')

students = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}


def make_student_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):
        return {k: v for (k, v) in exam_dict.items() if lower_bound <= v < upper_bound}

    return classify_student


grade_A = make_student_classifier(80, 100)
grade_B = make_student_classifier(70, 80)
grade_C = make_student_classifier(50, 70)
grade_D = make_student_classifier(0, 50)
print(grade_A(students))
print(grade_B(students))
print(grade_C(students))
print(grade_D(students))
