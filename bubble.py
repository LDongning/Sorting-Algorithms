# bubble.py
# -*- coding: utf-8 -*-

class bubble:
    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, arr):
        """
        冒泡排序主函数
        算法描述：
        1、比较相邻的元素。如果第一个比第二个大，就交换它们两个；
        2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        3、针对所有的元素重复以上的步骤，除了最后一个；
        4、重复步骤1~3，直到排序完成。
        :param arr:输入需要排序的一维数组
        :param reverse: False：从小到大排序，True：从大到小排序
        :return:
        """
        if type(arr) != list:
            return "Error: the type of array is not list"
        else:
            for i in range(len(arr) - 1):
                for j in range(len(arr) - i - 1):
                    if self.reverse == False:
                        if arr[j] > arr[j + 1]:
                            temp = arr[j+1]
                            arr[j + 1] = arr[j]
                            arr[j] = temp
                    else:
                        if arr[j] < arr[j + 1]:
                            temp = arr[j+1]
                            arr[j + 1] = arr[j]
                            arr[j] = temp
        return arr


if __name__ == '__main__':
    maopao = bubble(True)
    re = maopao.sorted([1, 3, 10, 0, 40, 2])
    print(re)
