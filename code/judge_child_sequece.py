class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 贪心策略，双指针，分别指向s和t的下标，如果s[i]==t[j]则意味着找到了匹配的长度；但是无论是否匹配，t的下标指针j都必须往前移动。这样即兼顾了位置，也兼顾了长度
        n, m = len(s), len(t)
        i, j = 0, 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == n


s = Solution()
print(s.isSubsequence('ace', 'ahegdc'))
print(s.isSubsequence('aec', 'ahegdc'))
print(s.isSubsequence("axc", "ahbgdc"))