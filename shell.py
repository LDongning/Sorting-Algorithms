# shell.py
# -*- coding: utf-8 -*-

class shell:
    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, arr):
        '''
        希尔排序
        1、选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
        2、按增量序列个数k，对序列进行k 趟排序；
        3、每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。
        仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
        时间复杂度：最坏n^2 ,最好n, 平均n^1.3
        :param arr:
        :return:
        '''
        if type(arr) != list:
            return "Error: the type of arr is not list"
        else:
            len_arr = len(arr)
            dk = int(len_arr / 2)
            while (dk >= 1):
                for i in range(dk, len_arr):  # 从下标为dk的数进行插入排序
                    position = i
                    current_val = arr[position]  # 要插入的数

                    if self.reverse == False:
                        # position-dk,要插入的数的下标必须得大于等于0
                        while position - dk >= 0 and current_val < arr[position - dk]:
                            arr[position] = arr[position - dk]  # 往后移动
                            position = position - dk

                        else:
                            arr[position] = current_val
                    else:
                        while position - dk >= 0 and current_val > arr[position - dk]:
                            arr[position] = arr[position - dk]  # 往后移动
                            position = position - dk

                        else:
                            arr[position] = current_val

                print(">>:", arr)
                dk = int(dk / 2)

        return arr


if __name__ == '__main__':
    m = shell(True)
    re = m.sorted([7, 3, 10, 4, 40, 2, 2, 10.1])
    print(re)
