class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # 当前进次数大于n时，需要取余
        if k < 2:
            pass

        def swap(i, j, nums):
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        swap(0, n - 1, nums)
        swap(0, k - 1, nums)
        swap(k, n - 1, nums)

        print(nums)

s = Solution()
print(s.rotate([1, 2], 3))