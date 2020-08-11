class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        给定一个未排序的整数数组，找到最长递增子序列的个数。

        示例 1:

        输入: [1,3,5,4,7]
        输出: 2
        解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
                :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # 代表第一次遇到最长子序列
                        dp[i] = max(dp[i], dp[j] + 1)
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:  # 说明不是第一次遇到最长子序列，以[1,3,5,4,7]为例，5和4所在位置的最长子序列长度相同
                        count[i] += count[j]  # 相加的目的是因为第j个位置的最长子序列长度可能不为1，因此需要加上它

        max_dp = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i] == max_dp:  # 循环计算具有最长递增子序列长度的个数
                res += count[i]
        return res

