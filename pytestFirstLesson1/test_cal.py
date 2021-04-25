import pytest

from pytestFirstLesson1.cal import Calculator
import pytest


class TestCal:

    # 小数值整数相加
    def test_add(self):
        cal = Calculator()
        assert 3 == cal.add(1, 2)

    # 大数值整数相加
    def test_add1(self):
        cal = Calculator()
        assert 30000000 == cal.add(10000000, 20000000)

    # 小数添加
    def test_add2(self):
        cal = Calculator()
        assert 3.3 == cal.add(3.1, 0.2)

    # 负数相加
    def test_add3(self):
        cal = Calculator()
        assert -3 == cal.add(-1, -2)

    # 负数和正数相加
    def test_add4(self):
        cal = Calculator()
        assert 1 == cal.add(-1, 2)

    # 小数和整数相加
    def test_add5(self):
        cal = Calculator()
        assert 0.7 == cal.add(-1.3, 2)
