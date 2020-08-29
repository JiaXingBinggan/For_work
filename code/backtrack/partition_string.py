class Solution(object):
    def partition(self, s):
        """
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

        返回 s 所有可能的分割方案。

        示例:

        输入: "aab"
        输出:
        [
          ["aa","b"],
          ["a","a","b"]
        ]
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        res = []

        def backtrack(track, s):  # 回溯法
            if not s:
                res.append(track)

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:  # s[:i][::-1] # 反转
                    backtrack(track + [s[:i]], s[i:])

        backtrack([], s)

        return res