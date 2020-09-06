class Solution(object):
    def firstUniqChar(self, s):
        """
        在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return " "
        s_dict = {}
        for i, c in enumerate(s):
            if s_dict.get(c):
                s_dict[c][1] = s_dict[c][1] + 1
            else:
                s_dict.setdefault(c, [i, 1])

        num_1_c = []
        for key in s_dict:
            if s_dict[key][1] == 1:
                num_1_c.append([key, s_dict[key][0]])

        return sorted(num_1_c, key=lambda s: s[1])[0][0]

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_dict = {}
        for c in s:
            if c in s_dict: # 如果有了就要设为True
                s_dict[c] = True
            else:
                s_dict.setdefault(c, False)

        for c in s:
            if not s_dict[c]:
                return c

        return ' '

s = Solution()
print(s.firstUniqChar("abaccdeff"))
