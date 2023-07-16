# NUMBER = 5
PI = 3.14


def add_number(n1, n2):
    """Возвращает сложение двух чисел"""
    return n1 + n2


def sub_number(n1, n2):
    """Возвращает вычитание двух чисел"""
    return n1 - n2


def div_number(n1, n2):
    """Возвращает деление двух чисел"""
    # if n2 != 0:
    try:
        return n1 / n2
    except ZeroDivisionError:
        # else:
        print('На ноль делить нельзя')
        #     return False
        return False


def mul_number(n1, n2):
    """Возвращает умножение двух чисел"""
    return n1 * n2


def operations(n1, n2, act):
    try:
        return eval(f'{n1} {act} {n2}')
    except Exception:
        print('ERROR')
        return False
