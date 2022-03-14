# Задание 1 - Unit Testing
# Используя предложенную реализацию «калькулятора» на языке программирования Java (см. прикрепленный файл),
# напишите свою реализацию всех этих функций на Python. Напишите один или несколько юнит-тестов на каждый метод,
# чтобы обнаружить все ошибки реализации, существующие в текущей имплементации методов.

from calculator import *
import math as m
import pytest


class TestCalc:
    def test_int_sum(self):
        assert int_sum(4, 2) == sum([4, 2])
        assert int_sum(2.222, 1.555) == int(2.222) + int(1.555)
        assert int_sum(0, 2.71083e+10) == int(0) + int(2.71083e+10)
        assert int_sum(-4, -2) == sum([-4, -2])
        assert type(int_sum(2.5, 1.555)) == int

    @pytest.mark.parametrize("test_input,expected", [(('a', 4), ValueError),
                                                     ((2, 'b'), ValueError)])
    def test_check_int_sum(self, test_input, expected):
        with pytest.raises(ValueError):
            int_sum(*test_input)

    def test_float_sum(self):
        assert float_sum(4.558, 2.508) == sum([4.558, 2.508])
        assert float_sum(2.71083e-10, 4.13903e-10) == float(sum([2.71083e-10, 4.13903e-10]))
        assert float_sum(-4.558, -2.508) == float(sum([-4.558, -2.508]))
        assert float_sum(0, -2.508) == float(sum([0, -2.508]))
        assert type(float_sum(-4.558, -2.508)) == float

    #корректные значения ((5.5, 5.5), 11) оставила специально, проверить что тест пойдет дальше после
    @pytest.mark.parametrize("test_input,expected", [(('a', 4.558), ValueError),
                                                     ((2.508, "b"), ValueError),
                                                     ((5.5, 5.5), 11)])
    def test_check_float_sum(self, test_input, expected):
        with pytest.raises(ValueError):
            float_sum(*test_input)

    def test_int_sub(self):
        assert int_sub(4, 2) == 4 - 2
        assert int_sub(4.55, 2.222) == int(4.55) - int(2.222)
        assert int_sub(-4.55, -2.222) == int(-4.55) - int(-2.222)
        assert int_sub(0, -2.222) == int(0) - int(-2.222)
        assert int_sub(2.71083e+10, 4.13903e+10) == int(2.71083e+10) - int(4.13903e+10)
        assert type(int_sub(4.55, 2.222)) == int

    @pytest.mark.parametrize("test_input,expected", [(('a', 4.558), ValueError),
                                                     ((2.508, "b"), ValueError)])
    def test_check_int_sub(self, test_input, expected):
        with pytest.raises(ValueError):
            int_sub(*test_input)

    def test_float_sub(self):
        assert float_sub(4, 2) == 4 - 2
        assert float_sub(4.55, 2.222) == float(4.55) - float(2.222)
        assert float_sub(-4.55, -2.222) == float(-4.55) - float(-2.222)
        assert float_sub(0, -2.222) == float(0) - float(-2.222)
        assert float_sub(2.71083e-10, 4.13903e-10) == float(2.71083e-10) - float(4.13903e-10)
        assert type(float_sub(4.558, 2.508)) == float

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), ValueError),
                                                      ((2.508, "b"), ValueError)])
    def test_check_float_sub(self, test_input, expected):
        with pytest.raises(ValueError):
            float_sub(*test_input)

    def test_int_mult(self):
        assert int_mult(4, 2) == (4*2)
        assert int_mult(2.222, 1.555) == int(2.222) * int(1.555)
        assert int_mult(0, 2) == int(0) * int(2)
        assert int_mult(-4, 2) == int(-4) * int(2)
        assert int_mult(2.71083e+10, 4.13903e+10) == int(2.71083e+10) * int(4.13903e+10)
        assert type(int_mult(4, 2)) == int

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), ValueError),
                                                      ((2.508, "b"), ValueError)])
    def test_check_int_mult(self, test_input, expected):
        with pytest.raises(ValueError):
            int_mult(*test_input)

    def test_float_mult(self):
        assert float_mult(4.558, 2.508) == float(4.558) * float(2.508)
        assert float_mult(2, 4) == float(2.222) * float(1.555)
        assert float_mult(0, 2) == float(0) * float(2)
        assert float_mult(-4, 2) == float(-4) * float(2)
        assert float_mult(2.71083e+10, 4.13903e+10) == float(2.71083e+10) * float(4.13903e+10)
        assert type(float_mult(4.558, 2.508)) == float

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), TypeError),
                                                      ((2.508, "b"), TypeError)])
    def test_check_float_mult(self, test_input, expected):
        with pytest.raises(TypeError):
            float_mult(*test_input)

    def test_int_div(self):
        assert int_div(4, 2) == 4/2
        assert int_div(4.558, 2.508) == int(4.558) / int(2.508)
        assert int_div(0, 2.508) == int(0) / int(2.508)

        with pytest.raises(ZeroDivisionError):
            assert int_div(4, 0)

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), ValueError),
                                                      ((2.508, "b"), ValueError)])
    def test_check_int_div(self, test_input, expected):
        with pytest.raises(ValueError):
            int_div(*test_input)

    def test_float_div(self):
        assert float_div(4.558, 2.508) == float(4.558) / float(2.508)
        assert float_div(0, 2.508) == float(0) / float(2.508)
        assert float_div(-4.558, -2.508) == float(-4.558) / float(-2.508)
        assert float_div(2.71083e-10, 4.13903e-10) == float(2.71083e-10) / float(4.13903e-10)

        with pytest.raises(ZeroDivisionError):
            float_div(4.558, 0)

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), ValueError),
                                                      ((2.508, "b"), ValueError)])
    def test_check_float_div(self, test_input, expected):
        with pytest.raises(ValueError):
            float_div(*test_input)

    def test_float_pow(self):
        assert float_pow(4.558, 2.508) == pow(4.558, 2.508)
        assert float_pow(-4.558, -2.508) == pow(-4.558, -2.508)
        assert float_pow(4.558, 0) == pow(4.558, 0)

        with pytest.raises(ValueError):
            float_pow(0, -3)

    @pytest.mark.parametrize("test_input, expected", [(('a', 4.558), TypeError),
                                                      ((2.508, "b"), TypeError)])
    def test_check_float_pow(self, test_input, expected):
        with pytest.raises(TypeError):
            float_pow(*test_input)

    def test_float_sqrt(self):
        assert float_sqrt(4.558) == m.sqrt(4.558)
        assert float_sqrt(-4.558) == m.sqrt(-4.558)
        assert float_sqrt(1000) == m.sqrt(1000)

    @pytest.mark.parametrize("test_input, expected", [('a', TypeError)])
    def test_check_float_sqrt(self, test_input, expected):
        with pytest.raises(TypeError):
            float_sqrt(*test_input)

    def test_float_ctg(self):
        assert float_ctg(4.558) == 1 / m.tan(4.558)
        assert float_ctg(2.71083e+10) == 1 / m.tan(2.71083e+10)

    @pytest.mark.parametrize("test_input, expected", [('a', TypeError)])
    def test_check_float_ctg(self, test_input, expected):
        with pytest.raises(TypeError):
            float_ctg(*test_input)

    def test_float_cos(self):
        assert float_cos(4.558) == m.cos(4.558)
        assert float_cos(4.558e+10) == m.cos(4.558e+10)

    @pytest.mark.parametrize("test_input, expected", [('a', TypeError)])
    def test_check_float_cos(self, test_input, expected):
        with pytest.raises(TypeError):
            float_cos(*test_input)

    def test_float_sin(self):
        assert float_sin(4.558) == m.sin(4.558)
        assert float_sin(4.558e+10) == m.sin(4.558e+10)

    @pytest.mark.parametrize("test_input, expected", [('a', ValueError)])
    def test_check_float_sin(self, test_input, expected):
        with pytest.raises(TypeError):
            float_sin(*test_input)
