# merge.py
# -*- coding: utf-8 -*-

class merge:
    """
    归并排序,分治法，将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
    算法描述：
    1、把长度为n的输入序列分成两个长度为n/2的子序列；
    2、对这两个子序列分别采用归并排序；
    3、将两个排序好的子序列合并成一个最终的排序序列。
    """

    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, lst):
        if len(lst) <= 1:
            return lst  # 从递归中返回长度为1的序列

        middle = int(len(lst) / 2)
        left = self.sorted(lst[:middle])  # 通过不断递归，将原始序列拆分成n个小序列
        right = self.sorted(lst[middle:])
        print(left, right)
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:  # 比较传入的两个子序列，对两个子序列进行排序
            if self.reverse == False:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            else:
                if left[0] >= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))

        # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
        result.extend(left)
        result.extend(right)

        return result


if __name__ == '__main__':
    m = merge(True)
    re = m.sorted([7, 2, 3, 10, 4, 40, 2, 10.1, 0])
    print(re)
