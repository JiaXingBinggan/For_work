class Solution(object):
    def findMagicIndex(self, nums):
        """魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
        :type nums: List[int]
        :rtype: int
        """
        min_index = 0
        first, last = 0, len(nums)
        mid = (first + last) // 2

        i = 0
        while i < mid: # 二分法，先找前一半，再找后一半
            if nums[i] == i:
                return i
            i += 1

        while i < len(nums):
            if nums[i] == i:
                return i
            i += 1

        return -1