class Solution:
    def chooseSort(self, unorderedList):
        '''
        选择排序，其只将最大项的位置记录下来，每一趟仅交换一次
        :param unorderedList:
        :return:
        '''
        for pass_num in range(len(unorderedList) - 1, 0, -1):
            max_location = 0
            for i in range(pass_num + 1): # 至少要有pass_num + 1个数字
                if unorderedList[i] > unorderedList[max_location]:
                    max_location = i

            temp = unorderedList[pass_num]
            unorderedList[pass_num] = unorderedList[max_location]
            unorderedList[max_location] = temp

        orderedList = unorderedList

        return orderedList

s = Solution()
print(s.chooseSort([2, 4, 2, 6, 3, 8, 19, 12]))