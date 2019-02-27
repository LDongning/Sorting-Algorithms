# heap.py
# -*- coding: utf-8 -*-

class heap:
    '''
    堆是一棵顺序存储的完全二叉树。

    其中每个结点的关键字都不大于其孩子结点的关键字，这样的堆称为小根堆。

    其中每个结点的关键字都不小于其孩子结点的关键字，这样的堆称为大根堆。

    堆排序
    （1）根据初始数组去构造初始堆（构建一个完全二叉树，保证所有的父结点都比它的孩子结点数值大）。

    （2）每次交换第一个和最后一个元素，输出最后一个元素（最大值），然后把剩下元素重新调整为大根堆。

    时间复杂度：平均 nlog(n),最坏 nlog(n),最好 nlog(n)，不稳定
    '''

    def __init__(self, reverse=False):
        self.reverse = reverse

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    def buildHeap_min(self, arr, i, len):
        # 最小堆的实现
        k = 2 * i + 1
        temp = arr[i]
        while (k < len):
            if k + 1 < len:
                # 从左子节点往右子节点扫描
                if arr[k] > arr[k + 1]:
                    k = k + 1
            # 从子节点往父节点扫描，子节点与父节点值替换
            if arr[k] < temp:
                self.swap(arr, i, k)
                i = k
            else:
                break
            k = 2 * k + 1

        return arr

    def buildHeap_max(self, arr, i, len):
        # 最大堆的实现
        k = 2 * i + 1
        temp = arr[i]
        while (k < len):
            if k + 1 < len:
                if arr[k] < arr[k + 1]:
                    k = k + 1

            if arr[k] > temp:
                self.swap(arr, i, k)
                i = k
            else:
                break
            k = 2 * k + 1

        return arr

    def sorted(self, arr):

        # 初始化堆，
        for i in range(int(len(arr) / 2) - 1, -1, -1):
            if self.reverse == False:
                self.buildHeap_max(arr, i, len(arr))
            else:
                self.buildHeap_min(arr, i, len(arr))

        # 每次循环取出当前堆中最小或最大值，与数组最后一个元素交换
        for j in range(len(arr) - 1, 0, -1):

            self.swap(arr, 0, j)

            if self.reverse == False:
                self.buildHeap_max(arr, 0, j)
            else:
                self.buildHeap_min(arr, 0, j)

        return arr


if __name__ == '__main__':
    arr = [7, 2, 3, 10, 4, 40, 2, 10.1, 0, -99, 41, 9]
    m = heap(True)
    re = m.sorted(arr)
    print(re)
