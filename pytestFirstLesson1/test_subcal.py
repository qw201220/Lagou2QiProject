import pytest

from pytestFirstLesson1.cal import Calculator
import pytest


class TestSubCal:

    # 2小数值整数相减
    def test_sub(self):
        cal = Calculator()
        assert 1 == cal.sub(2, 1)

    # 大数值整数相减
    def test_sub1(self):
        cal = Calculator()
        assert 10000000 == cal.sub(20000000, 10000000)

    # 小数-大数
    def test_sub2(self):
        cal = Calculator()
        assert -4 == cal.sub(5, 9)

    # 负数-负数
    def test_sub3(self):
        cal = Calculator()
        assert 1 == cal.sub(-1, -2)

    # 负数-正数
    def test_sub4(self):
        cal = Calculator()
        assert -3 == cal.sub(-1, 2)

    # 小数和小数相加
    def test_sub5(self):
        cal = Calculator()
        assert 1.1 == cal.sub(1.4, 0.3)
