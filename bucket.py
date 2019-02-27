# bucket.py
# -*- coding: utf-8 -*-

from sort_methods.quick import quick


class bucket:
    '''
    桶排序 ：
    假设输入数据服从均匀分布，将数据分到有限数量的桶里
    每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
    算法描述：
    1、设置一个定量的数组当作空桶；
    2、遍历输入数据，并且把数据一个一个放到对应的桶里去；
    3、对每个不是空的桶进行排序；
    4、从不是空的桶里把排好序的数据拼接起来。
    时间复杂度：最好n，最坏n^2，平均 n+k
    '''

    def __init__(self, reverse=False):
        self.reverse = reverse

    def sorted(self, arr, bucket_size=5):
        if len(arr) == 0:
            return arr

        max_value = arr[0]
        min_value = arr[0]
        # 设置最小、最大值范围
        for ele in arr:
            if max_value < ele:
                max_value = ele
            if min_value > ele:
                min_value = ele

        # 构造桶
        bucketCount = int((max_value - min_value) / bucket_size) + 1
        bucket_arr = [[] for i in range(bucketCount)]

        # 在对应的每个桶里添加数据
        for ele in arr:
            bucket_arr[int((ele - min_value) / bucket_size)].append(ele)

        # 对每个桶里的数据进行排序
        m = quick(self.reverse)
        result = []
        for j in range(len(bucket_arr)):
            # 可以结合其它排序方法
            temp = m.sorted(bucket_arr[j], 0, len(bucket_arr[j]) - 1)
            if temp != None:
                result.extend(temp)

        return result


if __name__ == '__main__':
    arr = [7, 2, 3, 10, 4, 40, 2, 10, 0, 99, 41, 9]
    m = bucket(False)
    re = m.sorted(arr)
    print(re)
