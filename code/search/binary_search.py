class Solution:
    def binarySearch(self, orderedList, targetNum):
        '''
        二分查找（基于有序列表）
        :param orderedList: 有序表
        :param targetNum: 查找项
        :return: 查找结果True还是False
        '''
        first = 0
        final = len(orderedList) - 1

        found = False
        while first <= final and not found: # first <= final 这个条件很重要，用于停止
            mid = (first + final) // 2
            if targetNum == orderedList[mid]:
                found = True
            elif targetNum < orderedList[mid]:
                final = mid - 1
            else:
                first = mid + 1

        return found

    def binarySearchRecurrence(self, ordered_list, target_num):
        '''
        二分查找的递归版本
        :param ordered_list:
        :param target_num:
        :return:
        '''
        if len(ordered_list) == 0: # 结束条件
            return False
        elif len(ordered_list) == 1: # 另一种结束条件
            if target_num == ordered_list[0]:
                return True
            else:
                return False
        else:
            mid = len(ordered_list) // 2
            if ordered_list[mid] == target_num:
                return True
            elif ordered_list[mid] > target_num:
                return self.binarySearchRecurrence(ordered_list[:mid], target_num) # 切片操作的时间复杂度为o(k)，可能会使得算法复杂度增加
            else:
                return self.binarySearchRecurrence(ordered_list[(mid + 1):], target_num)

s = Solution()
print(s.binarySearch([1, 2, 5, 6, 7, 39, 45, 46], 3))
print(s.binarySearchRecurrence([1, 2, 5, 6, 7, 39, 45, 46], 39))