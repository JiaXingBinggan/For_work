class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''

        s = sorted(list(map(str, nums)))

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                print(s[i])
                if s[i] + s[j] > s[j] + s[i]:
                    s[i], s[j] = s[j], s[i]

        return ''.join(s)

s = Solution()
print(s.minNumber([128,12,320,32]))
print(s.minNumber([3,30,34,5,9]))
print(s.minNumber([10, 2]))
print(s.minNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
print(s.minNumber([5,54,52,67,68,5,52,17,93,53]))