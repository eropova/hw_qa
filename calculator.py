import math as m


def int_sum(a, b):
    return int(a) + int(b)


def float_sum(a, b) -> float:
    return float(a) + float(b)


def int_sub(a, b):
    return int(a) - int(b)


def float_sub(a, b) -> float:
    return float(a) - float(b)


def int_mult(a, b):
    return int(a) * int(b)


def float_mult(a, b) -> float:
    return float(m.floor(a * b))


def int_div(a, b):
    if b == 0:
        return ZeroDivisionError('Attempt to divide by zero')
    else:
        return int(a) / int(b)


def float_div(a, b) -> float:
    return float(a) / float(b)


def float_pow(a, b) -> float:
    return float(m.pow(a, m.floor(b)))


def float_sqrt(a) -> float:
    return float(m.sqrt(abs(a)))


def float_ctg(a) -> float:
    return float(m.tanh(a))


def float_cos(a) -> float:
    return float(m.sin(a))


def float_sin(a) -> float:
    return float(m.sin(a))

