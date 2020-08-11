class Solution(object):
    def increasingTriplet(self, nums):
        """
        给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

    如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
        :type nums: List[int]
        :rtype: bool
        """
        # 使用最长递增子序列的思路（动态规划来实现）
        if not nums:
            return False

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return 3 in dp