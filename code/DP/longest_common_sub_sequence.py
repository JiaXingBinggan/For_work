class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

        若这两个字符串没有公共子序列，则返回 0。
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)

        dp_table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp_table[i][j] = 1 + dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

        return dp_table[-1][-1]

s = Solution()
print(s.longestCommonSubsequence('asdfas', 'werasdfaswer'))
print(s.longestCommonSubsequence('bacefaebcdfabfaadebdaacabbdabcfffbdcebaabecefddfaceeebaeabebbad',
'dedcecfbbbecaffedcedbadadbbfaafcafdd'))