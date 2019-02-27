# selection.py
# -*- coding: utf-8 -*-

class selection:
    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, arr):
        '''
        选择排序主函数
        算法描述：
        1、初始状态：无序区为R[1..n]，有序区为空；
        2、第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
        该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
        使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
        3、n-1趟结束，数组有序化了。
        :param arr:输入需要排序的一维数组
        :param reverse: False：从小到大排序，True：从大到小排序
        :return:
        时间复杂度：最好n，最坏n^2，平均 n^2
        '''

        if type(arr) != list:
            return "Error: the type of array is not list"

        else:
            for i in range(len(arr) - 1):
                Index = i
                for j in range(i+1, len(arr) - i - 1):
                    if self.reverse == False:
                        if arr[j] < arr[Index]:
                            Index = j
                    else:
                        if arr[j] > arr[Index]:
                            Index = j
                temp = arr[i]
                arr[i] = arr[Index]
                arr[Index] = temp

        return arr


if __name__ == '__main__':
    m = selection(True)
    re = m.sorted([1, 3, 10, 0, 40, 2])
    print(re)
