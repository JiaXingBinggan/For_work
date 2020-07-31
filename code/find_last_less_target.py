class Solution(object):
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
nums = [10,26,30,31,32,34,47,60]
print(s.searchQtTarget(0, len(nums) - 1, nums, 40))