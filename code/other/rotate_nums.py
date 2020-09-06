class Solution(object):
    def rotate(self, nums, k):
        """
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

        示例 1:

        输入: [1,2,3,4,5,6,7] 和 k = 3
        输出: [5,6,7,1,2,3,4]
        解释:
        向右旋转 1 步: [7,1,2,3,4,5,6]
        向右旋转 2 步: [6,7,1,2,3,4,5]
        向右旋转 3 步: [5,6,7,1,2,3,4]

        示例 2:

        输入: [-1,-100,3,99] 和 k = 2
        输出: [3,99,-1,-100]
        解释:
        向右旋转 1 步: [99,-1,-100,3]
        向右旋转 2 步: [3,99,-1,-100]
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
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

    def rotate2(self, nums, k):
        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)

        print(nums)

s = Solution()
s.rotate2([1, 2], 3)


