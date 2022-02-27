import math as m


def int_sum(a, b):
    return a + b


def float_sum(a, b):
    return a + b


def int_sub(a, b):
    return a - b


def float_sub(a, b):
    return a - b


def int_mult(a, b):
    return a * b


def float_mult(a, b):
    return m.floor(a * b)


def int_div(a, b):
    if b == 0:
        return ZeroDivisionError
    else:
        return a / b


def float_div(a, b):
    return a / b


def float_pow(a, b):
    return m.pow(a, m.floor(b))


def float_sqrt(a):
    return m.sqrt(abs(a))


def float_ctg(a):
    return m.tanh(a)


def float_cos(a):
    return m.sin(a)


def float_sin(a):
    return m.sin(a)


# functions_m = ['int_sum', 'float_sum', 'int_sub', 'float_sub',
#                'int_mult', 'float_mult', 'int_div', 'float_div',
#                'float_pow']
# functions_s = ['float_sqrt', 'float_ctg', 'float_cos', 'float_sin']

# for f in functions_m:
#     print(f, eval(f'{f}(4, 2)'))
#
# for f in functions_s:
#     print(f, eval(f'{f}(5)'))

import inspect
print(inspect.signature(int_sum))