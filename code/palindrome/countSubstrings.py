class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        nums = 0

        def extend(i, j, s):
            num = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                num += 1

            return s[i + 1: j], num

        for i in range(n):
            p1, num1 = extend(i, i, s)
            p2, num2 = extend(i, i + 1, s)
            nums += (num1 + num2)

        return nums