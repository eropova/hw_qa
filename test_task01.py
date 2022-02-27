# Задание 1 - Unit Testing
# Используя предложенную реализацию «калькулятора» на языке программирования Java (см. прикрепленный файл),
# напишите свою реализацию всех этих функций на Python. Напишите один или несколько юнит-тестов на каждый метод,
# чтобы обнаружить все ошибки реализации, существующие в текущей имплементации методов.

from calculator import *
import math as m
import pytest


def test_int_sum():
    assert int_sum(4, 2) == sum([4, 2])
    with pytest.raises(TypeError):
        int_sum('a', 1.555)
        int_sum(2.222, 1.555)


def test_float_sum():
    assert float_sum(4.558, 2.508) == sum([4.558, 2.508])
    with pytest.raises(TypeError):
        float_sum('a', 2)
        float_sum(4, 2)


def test_int_sub():
    assert int_sub(4, 2) == 4 - 2
    with pytest.raises(TypeError):
        int_sub('a', 1.555)


def test_float_sub():
    assert float_sub(4.558, 2.508) == 4.558 - 2.508
    with pytest.raises(TypeError):
        float_sub('a', 2)

def test_int_mult():
    assert int_mult(4, 2) == (4*2)
    with pytest.raises(TypeError):
        int_mult('a', 1.555)


def test_float_mult():
    assert float_mult(4.558, 2.508) == 4.558 * 2.508
    with pytest.raises(TypeError):
        float_mult('a', 2)


def test_int_div():
    assert int_div(4, 2) == 4/2
    assert int_div(4, 0) == ZeroDivisionError
    with pytest.raises(TypeError):
        int_div('a', 1.555)


def test_float_div():
    assert float_div(4.558, 2.508) == 4.558 / 2.508
    assert float_div(4.558, 0) == ZeroDivisionError
    with pytest.raises(TypeError):
        float_div('a', 2)


def test_float_pow():
    assert float_pow(4.558, 2.508) == pow(4.558, m.floor(2.508))
    with pytest.raises(TypeError):
        float_pow('a', 2)


def test_float_ctg():
    assert float_ctg(4.558) == 1 / m.tan(4.558)
    with pytest.raises(TypeError):
        float_ctg('a')
        float_ctg(2)


def test_float_cos():
    assert float_cos(4.558) == m.cos(4.558)
    with pytest.raises(TypeError):
        float_cos('a')
        float_cos(2)


def test_float_sin():
    assert float_sin(4.558) == m.sin(4.558)
    with pytest.raises(TypeError):
        float_sin('a')
        float_sin(2)
