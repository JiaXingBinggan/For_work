class Solution:
    def insertSort(self, unorderedList):
        '''
        插入排序，其思想就是寻找新项的插入位置
        :param unorderedList:
        :return:
        '''
        for index, num in enumerate(unorderedList):
            position = index

            # 从第2个开始寻找新项
            while position > 0 and num < unorderedList[position - 1]:
                unorderedList[position] = unorderedList[position - 1] # 如果前一项比它大，则把当前位置赋值为上一个位置的值，以表示往后移动
                position -= 1

            unorderedList[position] = num # 插入新项，因为比它大的值，都移到了position之后

        orderedList = unorderedList

        return orderedList

    def insertSort2(self, unorderedList):
        for index, num in enumerate(unorderedList):
            position = index
            while position and unorderedList[position - 1] > num:
                unorderedList[position] = unorderedList[position - 1]
                position -= 1

            unorderedList[position] = num
        return unorderedList



s = Solution()
print(s.insertSort([34, 23, 45, 67, 12, 11]))
print(s.insertSort2([34, 23, 45, 67, 12, 11]))