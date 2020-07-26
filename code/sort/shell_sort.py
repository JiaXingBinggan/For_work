class Solution:
    def shellSort(self, unorderedList):
        '''
        谢尔排序，其把list划分多个子列表，每个子列表进行插入排序
        :param unorderedList:
        :return:
        '''
        split_count = len(unorderedList) // 2 # 分割子列表大小
        while split_count > 0:
            for i in range(split_count):
                self.inserSort(unorderedList, i, split_count)
            print(unorderedList)

            split_count = split_count // 2 # 持续缩小

        return unorderedList


    def inserSort(self, unorderedList, start, gap):
        '''
        :param unorderedList:
        :return:
        '''
        for index in range(start, len(unorderedList), gap):
            position = index # 当前位置
            current_num = unorderedList[index]

            while position > start and current_num < unorderedList[position - gap]: # 注意，这里一定要弄成position
                unorderedList[position] = unorderedList[position - gap] # 带间隔gap
                position -= gap

            unorderedList[position] = current_num

s = Solution()
print(s.shellSort([13, 4, 5, 3, 35, 12, 2, 6, 16]))
