class Solution(object):
    def search(self, nums, target):
        """
        统计一个数字在排序数组中出现的次数。
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分法解题
        # https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        while left <= right: # 求右边界
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0 and nums[right] != target:
            return 0

        upper_bound = left

        left = 0
        while left <= right: # 求左边界
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        lower_bound = right

        return upper_bound - lower_bound - 1

