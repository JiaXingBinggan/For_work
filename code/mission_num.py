class Solution(object):
    def missingNumber(self, nums):
        """
        看到排序过的列表，需要进行查找，就要想到二分法
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == mid:
                first = mid + 1
            else:
                last = mid - 1

        return first

s = Solution()
print(s.missingNumber([0, 1, 3]))