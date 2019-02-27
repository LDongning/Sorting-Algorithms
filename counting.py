# Counting.py
# -*- coding: utf-8 -*-

class count:
    '''
    计数排序：
    其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
    作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
    算法描述：
    1、找出待排序的数组中最大和最小的元素；
    2、统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
    3、对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
    4、反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
    局限性：大于等于零的正整数，时间复杂度和空间复杂度都是 n+k
    '''

    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, arr):
        # 找出最大值
        maxValue = 0
        for ele in arr:
            if ele > maxValue:
                maxValue = ele

        # 构建临时数组
        temp = [0 for i in range(maxValue + 1)]

        # 计数
        for ele in arr:
            temp[ele] = temp[ele] + 1

        # 排序
        index = 0
        if self.reverse == False:
            for i in range(len(temp)):
                while (temp[i] > 0):
                    arr[index] = i
                    temp[i] = temp[i] - 1
                    index = index + 1
        else:
            for i in range(len(temp)-1, -1, -1):
                while (temp[i] > 0):
                    arr[index] = i
                    temp[i] = temp[i] - 1
                    index = index + 1

        return arr


if __name__ == '__main__':
    arr = [7, 2, 3, 10, 4, 40, 2, 10, 0, 99, 41, 9]
    m = count(True)
    re = m.sorted(arr)
    print(re)
