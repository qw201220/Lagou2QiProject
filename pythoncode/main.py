have_girl = False
def noParamMethod1():
    print("这是一个无返回值的无参方法")
def noParamMethod2():
    print("这是一个有返回值的无参方法")
    return "这是一个有返回值的无参方法"

def paramMethod1(param):
    print("这是一个无返回值的有参方法: %s" %param)

def paramMethod2(param):
    print("这是一个有返回值的有参方法: %s" %param)
    return param




if __name__ == '__main__':
    print(__name__)
    print(noParamMethod1())
    print("..............................................")
    print(noParamMethod2())
    print("..............................................")
    print(paramMethod1("有参无返回值"))
    print("..............................................")
    print(paramMethod2("有参有返回值"))
