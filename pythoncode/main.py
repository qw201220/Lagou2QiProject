have_girl = False
def send():
    print("发女朋友啦。。")
    global have_girl
    have_girl = True
    print(f"have_girl = {have_girl}")


def show():
    if have_girl == True:
        print("有女朋友，好开心~~")
    else:
        print("单身贵族 *__*")



if __name__ == '__main__':
    print(__name__)
    send()
    show()