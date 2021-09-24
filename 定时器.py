import threading
import queue
import time
from func_timeout import func_set_timeout
import func_timeout


@func_set_timeout(3)  # 设定函数超执行时间_
def task():
    print('hello world')
    while 1:
        time.sleep(1)
        print(1)
    return '执行成功_未超时'


if __name__ == '__main__':
    try:
        print(task())
    #若调用函数超时自动走异常(可在异常中写超时逻辑处理)
    except func_timeout.exceptions.FunctionTimedOut:
        print('执行函数超时')
    # print(task())


import eventlet
def timeou(name, _time):
    eventlet.monkey_patch()  # 必须加这条代码
    with eventlet.Timeout(_time, False):  # 设置超时间
        time.sleep(2)
        if isinstance(name, str):
            print('name为字符串类型_值是{}'.format(name))
            return 'str'
        else:
            print('‘name类型为:{}'.format(eval(str(type(name)).split()[1][:-1])))
            return eval(str(type(name)).split()[1][:-1])
    print('不好意思函数调用超时')
# if __name__ == '__main__':
#     print(timeou('‘你好靓女！‘', 1))
