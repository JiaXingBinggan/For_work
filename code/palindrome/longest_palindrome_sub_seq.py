class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp[i][j]表示s[i..j]字符子串中的最长回文子序列

        for i in range(n):  # dp[i][i]为只有一个字符，那么它的最长回文子序列肯定为自己，长度为1
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):  # 反着进行
            for j in range(i + 1, n):  # j必须比i大，因此从i + 1开始
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2  # 因为s[i]=s[j]则最长回文子序列在s[i+1 .. j-1]的最长回文子序列的基础上加上两个字符的长度
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][
                        j - 1])  # 如果它俩不相等，说明它俩不可能同时出现在 s[i..j] 的最长回文子序列中，那么把它俩分别加入 s[i+1..j-1] 中，看看哪个子串产生的回文子序列更长即可

        return dp[0][n - 1]  # 返回字符串的最长公共子序列长度