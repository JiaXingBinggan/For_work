class Solution(object):
    def longestPalindrome(self, s):
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

        示例 1：

        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        n = len(s)
        res = s[0]

        def extend(i, j, s):
            while i >= 0 and j < n and s[i] == s[j]:  # 扩展，如果一个或两个数为回文字符子串，那么只需要判断外围是不是回文字符子串
                i -= 1
                j += 1

            return s[i + 1: j]  # 因为while判断停止，所以需要回溯下标

        for i in range(n - 1):
            p1 = extend(i, i, s)
            p2 = extend(i, i + 1, s)  # 有可能相邻两个字符为相同的字符

            if max(len(p1), len(p2)) > len(res):  # 选择最长的子串
                res = p1 if len(p1) > len(p2) else p2

        return res