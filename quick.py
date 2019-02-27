# merge.py
# -*- coding: utf-8 -*-

class quick:
    '''
    快速排序算法：
    每次排序的时候设置一个基准点，将小于等于基准点的数全部放到基准点的左边，将大于等于基准点的数全部放到基准点的右边。
    每次排序的过程，都是寻找基准点的位置的过程。
    每次排序从最右侧向左开始扫描。
    时间复杂度：平均 nlog(n),最坏 n^2,最好 n，不稳定
    '''
    def __init__(self, reverse=False):
        self.reverse = reverse

    # 快速排序 传入列表、开始位置和结束位置
    def sorted(self, arr, start, end):

        if not start < end:
            return None

        mid = arr[start]  # 拿出第一个数当作基准数mid
        left = start
        right = end

        # 进行循环，目的是寻找基准位置，左边的数值永远比基准小，右边的位置永远比基准大
        # 当left和right相等，说明碰头了，且找到了此时的基准位置
        while left != right:
            if self.reverse==False:
                # 从right开始向左，找到第一个比mid小或者等于mid的数，标记位置
                while left < right and arr[right] > mid:
                    right -= 1
                # 跳出while后，right所在的下标就是找到的右侧比mid小的数

                # 从left开始向右，找到第一个比mid大的数，标记位置
                while left < right and arr[left] <= mid:
                    left += 1
                # 跳出while循环后left所在的下标就是左侧比mid大的数所在位置
            else:
                # 由大到小排列
                while left < right and arr[right] < mid:
                    right -= 1

                while left < right and arr[left] >= mid:
                    left += 1

            # 交换两个数在数组中的位置
            if left < right:
                t = arr[left]
                arr[left] = arr[right]
                arr[right] = t

                # 以上我们完成了一次 从右侧找到一个小数移到左侧，从左侧找到一个大数移动到右侧

        # 当这个while跳出来之后相当于left和right碰头了，我们把mid所在位置放在这个找出来的基准位置

        arr[start] = arr[left]
        arr[left] = mid
        # 这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大

        # 然后我们对mid左侧所有数进行上述的排序
        self.sorted(arr, start, left - 1)
        # 我们mid右侧所有数进行上述排序
        self.sorted(arr, left + 1, end)

        return arr


if __name__ == '__main__':
    arr = [7, 2, 3, 10, 4, 40, 2, 10.1, 0]
    m = quick(True)
    re = m.sorted(arr, 0, len(arr) - 1)
    print(re)
