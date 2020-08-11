class Solution(object):
    def threeSum(self, nums):
        """
        https://leetcode-cn.com/problems/3sum/
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        if nums[0] > 0:
            return []

        res = []
        for i in range(len(nums)):
            current_num = nums[i]
            two_sum_arrs = self.two_sum(i + 1, len(nums) - 1, nums, 0 - current_num)
            for two_sum_arr in two_sum_arrs:
                if sorted(two_sum_arr + [current_num]) not in res:
                    res.append(sorted(two_sum_arr + [current_num]))

        return res

    def two_sum(self, first, last, nums, target):
        current_res = []
        while first < last:
            sum_ = nums[first] + nums[last]
            if sum_ > target:
                last -= 1
            elif sum_ < target:
                first += 1
            else:
                current_res.append([nums[first], nums[last]])
                first += 1
                last -= 1

        return current_res