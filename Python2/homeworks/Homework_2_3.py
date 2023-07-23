# Домашнее задание по теме декораторы:#
# Реализация функциональности декораторов в приложении Python#
# Планируемый результат:#
# Использование декораторов, для изменения поведения функции в языке Python

# Решение: Напишем декоратор, который будет повторять выполнение функции (заданное количество раз),
#  если она, по какой-то причине, завершится неудачно

import time
import random


def repeat(max_repeat):
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_repeat):
                try:
                    print(f'function start. attept:{_ + 1}  ')
                    func(*args, **kwargs)
                except:
                    time.sleep(1)

        return wrapper

    return repeat_decorator


@repeat(2)
def simulated_failure():
    print("might fail")
    # Имитация вызова исключения
    raise Exception


simulated_failure()


# Вариант с классом
# Декоратор-класс, который считает время работы функции.

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        self.func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f'function runtime {runtime:.4f} secs')


@Decorator
def bubble_sort(nums):
    """Функция реализует пузырьковую сортировку"""
    process = True
    while process:
        process = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                process = True


num = random.sample(range(1, 1000), 100)
print(f'List to sort\n{num}')
bubble_sort(num)
print(num)
