# main.py
# -*- coding: utf-8 -*-

from sort_methods.bubble import bubble
from sort_methods.selection import selection
import time


def sort(func, reverse):
    result = ''
    t1 = time.time()
    if reverse == 'True':
        m = func(True)
        result = m.sorted(a)
    else:
        m = func(False)
        result = m.sorted(a)
    t2 = time.time()
    print("排序结果：", result)
    print("排序耗时>>>{}s".format(t2 - t1))


if __name__ == '__main__':
    line = input('请输入需要排序的自然数，用空格分隔：')
    method = input('请输入排序方法名：')
    reverse = input('由大到小输入True,有小到大输入False:')
    a = ''
    try:
        a = line.split(" ")
    except:
        print("请用空格隔开每个自然数！")

    try:
        a = [float(i) for i in a]
        if method == 'bubble':
            sort(bubble, reverse)
        elif method == 'selection':
            sort(selection, reverse)
        else:
            print('排序方法不存在')
    except:
        print("输入非整数,请重新输入！")
