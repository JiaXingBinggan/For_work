class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        dp_num = [0] * len(s)
        dp_str = [''] * len(s)

        dp_num[0], dp_str[0] = 1, s[0]
        for i in range(1, len(s)):
            if s[i] not in dp_str[i - 1]:
                dp_str[i] = dp_str[i - 1] + s[i]
            else:
                origin_s_index = dp_str[i - 1].index(s[i])
                dp_str[i] = dp_str[i - 1][origin_s_index + 1:] + s[i]

            dp_num[i] = len(dp_str[i])

        return max(dp_num)

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring("dvdf"))