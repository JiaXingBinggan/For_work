class Solution(object):
    def twoSum(self, nums, target):
        """
        输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
        示例 1：

        输入：nums = [2,7,11,15], target = 9
        输出：[2,7] 或者 [7,2]
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0

        last = self.searchQtTarget(first, len(nums) - 1, nums, target) # 二分法找出列表中最后一个小于target的位置，因为大于target的数都可以直接舍去
        while first <= last: # 双指针，从列表的头和尾往中间靠拢；凡是此类有序数组的查找其实都可以用双指针
            s = nums[first] + nums[last]
            if s > target:
                last -= 1
            elif s < target:
                first += 1
            else:
                return [nums[first], nums[last]]

        return []

    def searchQtTarget(self, first, last, nums, target):
        '''
        找到列表中最后一个小于target的数
        :param first:
        :param last:
        :param nums:
        :param target:
        :return:
        '''
        if nums[last] < target:
            return last

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            else:
                if nums[mid - 1] <= target:
                    return mid - 1
                else:
                    last = mid - 1

s = Solution()
print(s.twoSum([10,26,30,31,32,34,47,60], 40))
print(s.twoSum([12,12,18,37,51,54], 30))