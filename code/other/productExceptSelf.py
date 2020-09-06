class Solution(object):
    def productExceptSelf(self, nums):
        """
        计算除自身以外的乘积，leetcode
        :type nums: List[int]
        :rtype: List[int]
        """
        left_mul = [0] * len(nums)
        right_mul = [0] * len(nums)
        left_mul[0] = 1
        right_mul[-1] = 1

        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if i != 0:
                left_mul[i] = left_mul[i - 1] * nums[i - 1]
        right_index = len(nums) - 2
        while right_index >= 0:
            right_mul[right_index] = right_mul[right_index + 1] * nums[right_index + 1]
            right_index -= 1
        print(left_mul, right_mul)
        for i, num in enumerate(nums):
            output[i] = left_mul[i] * right_mul[i]

        return output

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))