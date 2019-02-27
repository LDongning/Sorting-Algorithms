# insertion.py
# -*- coding: utf-8 -*-

class insertion:
    def __init__(self, reverse):
        self.reverse = reverse

    def sorted(self, arr):
        '''
        插入排序：
        1、从第一个元素开始，该元素可以认为已经被排序；
        2、取出下一个元素，在已经排序的元素序列中从后向前扫描；
        3、如果该元素（已排序）大于新元素，将该元素移到下一位置；
        4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
        5、将新元素插入到该位置后；
        6、重复步骤2~5。
        时间复杂度：最坏 n^2, 最好 n, 平均 n^2
        :param arr:
        :return:
        '''
        if type(arr) != list:
            return "Error: the type of array is not list"
        else:
            for i in range(1, len(arr)):
                preIndex = i - 1
                current = arr[i]
                if self.reverse == False:
                    while ((preIndex >= 0) & (arr[preIndex] > current)):
                        arr[preIndex + 1] = arr[preIndex]
                        preIndex = preIndex - 1
                else:
                    while ((preIndex >= 0) & (arr[preIndex] < current)):
                        arr[preIndex + 1] = arr[preIndex]
                        preIndex = preIndex - 1

                arr[preIndex + 1] = current

        return arr


if __name__ == '__main__':
    m = insertion(True)
    re = m.sorted([7, 3, 10, 4, 40, 2, 2, 10.1])
    print(re)
