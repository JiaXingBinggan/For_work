class Solution:
    def quickSort(self, unorderedList):
        '''
        快速排序
        :param unorderedList:
        :return:
        '''
        self.recurrenceSort(unorderedList, 0, len(unorderedList) - 1)

        return unorderedList

    def recurrenceSort(self, unorderedList, first, last):
        '''
        递归
        :param unorderedList:
        :param first:
        :param last:
        :return:
        '''
        if first < last: # 只剩下一个或者没有就停止了，因为如果只剩一个，则first=last
            new_split_index = self.position(unorderedList, first, last) # 求得中位值对应index，用于把列表分为两半

            self.recurrenceSort(unorderedList, first, new_split_index - 1)
            self.recurrenceSort(unorderedList, new_split_index + 1, last)

    def position(self, unorderedList, first, last):
        mid_num = unorderedList[first] # 取列表第一位作为中位值
        leftmark = first + 1 # 左标为mid_num下一位，逐步向右靠近
        rightmark = last # 右标为last，逐步向左靠近

        done = False
        while not done:
            while leftmark <= rightmark and unorderedList[leftmark] <= mid_num: # 当遇到比中位值大的则暂停，记录当前位置
                leftmark += 1

            while rightmark >= leftmark and unorderedList[rightmark] >= mid_num: # 当遇到比中位值小的则暂停，记录当前位置
                rightmark -= 1

            if leftmark > rightmark:
            # 如果左标大于右标则停止。这是因为左标总是遇到比中位值大的才停止，右标总是遇到比中位值小的才停止
            # 因此当左标大于右标时，右标指向的为最后一个比中位值小的值，然后，交换中位值和右标指的数，至此，中位值左边的都是比它小的，右边都是比它大的。
                done = True
            else: # 交换leftmark和rightmark对应数的位置
                temp = unorderedList[rightmark]
                unorderedList[rightmark] = unorderedList[leftmark]
                unorderedList[leftmark] = temp
        
        # 交换中位值和rightmark对应的数，这样中位值左边的所有数都小于中位值，右边的数都大于中位值
        temp = unorderedList[rightmark]
        unorderedList[rightmark] = mid_num
        unorderedList[first] = temp

        return rightmark

s = Solution()
print(s.quickSort([4, 3, 5, 2, 6, 1, 7, 6]))


