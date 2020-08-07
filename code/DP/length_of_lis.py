class Solution(object):
    def lengthOfLIS(self, nums):
        """
        给定一个无序的整数数组，找到其中最长上升子序列的长度。
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums) # 记录当前的最长上升子序列长度
        n = len(nums)

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]: # 每次大小较大时才比较
                    dp[i] = max(dp[i], dp[j] + 1) # 其实就是选择子序列中最长的那一个+1

        return max(dp)



