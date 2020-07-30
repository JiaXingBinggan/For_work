class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.strip().split(' ')

        while '' in list_s: # 处理边界条件
            list_s.remove('')

        first, last = 0, len(list_s) - 1

        while first < last:
            list_s[first], list_s[last] = list_s[last], list_s[first]
            first += 1
            last -= 1

        return ' '.join(tuple(list_s))

s = Solution()
print(s.reverseWords("  hello world!  "))
print(s.reverseWords("a good   example"))