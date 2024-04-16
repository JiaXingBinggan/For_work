"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。



示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序


进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题
"""
from typing import List

# 双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        first = 0
        last = len(nums) - 1
        idx = len(nums) - 1

        while first <= last:
            if nums[first] * nums[first] < nums[last] * nums[last]:
                results[idx] = nums[last] * nums[last]
                last -= 1
            else:
                results[idx] = nums[first] * nums[first]
                first += 1
            idx -= 1

        return results

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))