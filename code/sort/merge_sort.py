class Solution:
    def mergeSort(self, unorderedList):
        '''
        归并排序，递归思想
        :param unorderedList:
        :return:
        '''
        if len(unorderedList) <= 1: # 基本结束条件，当列表长度小于等于1时，则只剩1个数字，本身就已经排好序了
            return unorderedList

        # 二分分裂
        mid = len(unorderedList) // 2
        left = self.mergeSort(unorderedList[:mid])
        right = self.mergeSort(unorderedList[mid:])

        # 对已经划分好的left和right列表进行归并排序
        tempOrderedList = []
        while left and right:
            if left[0] < right[0]: # 拉链式交错排序
                tempOrderedList.append(left.pop(0))
            else:
                tempOrderedList.append(right.pop(0))

        # 如果left或者right列表还有剩，则直接extend在末尾，因为本身left和right都是已经排好序的，剩余的都是比已排好序的大的数字
        # 而且仅会存在left或者right中一个有剩的情况
        tempOrderedList.extend(left if left else right)

        return tempOrderedList

    def mergeSort2(self, unorderedList):
        if len(unorderedList) <= 1:
            return unorderedList

        mid = len(unorderedList) // 2
        left = self.mergeSort2(unorderedList[:mid])
        right = self.mergeSort2(unorderedList[mid:])

        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))

        res.extend(left if left else right)

        return res

s = Solution()
print(s.mergeSort([1,3,2,8,5,7, 4, 9, 0, 6]))
print(s.mergeSort2([1,3,2,8,5,7, 4, 9, 0, 6]))

