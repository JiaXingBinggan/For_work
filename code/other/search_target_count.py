class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first_equal_index = 0

        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                if nums[mid - 1] == target:
                    first_equal_index = mid - 1
                    break
                else:
                    last = mid - 1
            else:
                first_equal_index = mid
                break

        count = 0
        for i in range(first_equal_index, -1, -1):
            if nums[i] == target:
                count += 1
            else:
                break

        return count

s = Solution()
print(s.search([5,7,7,8,8,10], 8))
print(s.search([5,7,7,8,8,10], 6))