import pytest


@pytest.fixture(autouse=True)
def setup_teardown():
    print('开始计算：')
    a = 1
    yield a
    print('计算结束')
