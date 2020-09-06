class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        n = len(s)
        dp = [False] * (n + 1) # 也就是预先设置所有的字符串都不能被worddict表示
        dp[0] = True # 空字符串是可以表示的

        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    # 判断s[i:j]是否在worddict中，如果在然后如果dp[i]为True说明s[:j]能够用worddict表示
                    dp[j] = True

        return dp[-1]