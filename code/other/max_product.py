class Solution(object):
    def maxProduct(self, nums):
        """
        https://leetcode-cn.com/submissions/detail/102119350/
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        reverse_nums = nums[::-1]

        for i in range(1, n):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1

        return max(max(nums), max(reverse_nums))