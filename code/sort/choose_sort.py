class Solution:
    def chooseSort(self, unorderedList):
        '''
        选择排序，其只将最大项的位置记录下来，每一趟仅交换一次
        :param unorderedList:
        :return:
        '''
        for pass_num in range(len(unorderedList) - 1, -1, -1):
            max_location = 0
            for i in range(pass_num + 1):
                if unorderedList[i] > unorderedList[max_location]:
                    max_location = i

            unorderedList[pass_num], unorderedList[max_location] = unorderedList[max_location], unorderedList[pass_num]

        return unorderedList

    def chooseSort2(self, unorderedList):
        for pass_num in range(len(unorderedList) - 1, -1, -1):
            max_location = 0
            for i in range(1, pass_num + 1):
                if unorderedList[i] > unorderedList[max_location]:
                    max_location = i

            unorderedList[pass_num], unorderedList[max_location] = unorderedList[max_location], unorderedList[pass_num]

        return unorderedList


s = Solution()
print(s.chooseSort([2, 4, 2, 6, 3, 8, 19, 12]))
print(s.chooseSort2([2, 4, 2, 6, 3, 8, 19, 12]))