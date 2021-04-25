from pytestFirstLesson1.cal import Calculator


class TestDevCal:

    # 小整数/大整数
    def test_dev(self):
        cal = Calculator()
        assert 0.5 == cal.dev(1, 2)

    # 大整数/小整数
    def test_dev1(self):
        cal = Calculator()
        assert 2 == cal.dev(20000000, 10000000)

    # 小数相除
    def test_dev2(self):
        cal = Calculator()
        assert 5.5 == cal.dev(1.1, 0.2)

    # 负数相除
    def test_dev3(self):
        cal = Calculator()
        assert 0.5 == cal.dev(-1, -2)

    # 负数除以正数
    def test_dev4(self):
        cal = Calculator()
        assert -0.6 == cal.dev(-1.2, 2)

    # 0除以非0数
    def test_dev5(self):
        cal = Calculator()
        assert 0 == cal.dev(0, 0.1)
