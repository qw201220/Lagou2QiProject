from pytestFirstLesson1.cal import Calculator


class TestMulCal:

    # 整数相乘
    def test_mul(self):
        cal = Calculator()
        assert 2 == cal.mul(1, 2)

    # 0*任何数
    def test_mul1(self):
        cal = Calculator()
        assert 0 == cal.mul(0, 10000000)

    # 小数相乘
    def test_mul2(self):
        cal = Calculator()
        assert 0.22 == cal.mul(1.1, 0.2)

    # 负数相乘
    def test_mul3(self):
        cal = Calculator()
        assert 2 == cal.mul(-1, -2)

    # 负数乘正数
    def test_mul4(self):
        cal = Calculator()
        assert -2.4 == cal.mul(-1.2, 2)

    # 大数想相
    def test_mul5(self):
        cal = Calculator()
        assert 212121212121000000000 == cal.mul(1000000000, 212121212121)
