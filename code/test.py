class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                continue
            else:
                for j in range(i, n - 1):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        print(nums)


s = Solution()
print(s.moveZeroes([0, 0, 1]))
print(s.moveZeroes([0,1,0,3,12]))
