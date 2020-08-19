class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        num_c = {}
        for c in s:
            if c not in num_c:
                num_c.setdefault(c, 1)
            else:
                num_c[c] += 1

        # 用获得最长回文串的思路，如果该字符串能够获得的最长回文串的长度刚好等于s的长度，那么肯定就是一个回文串
        palindrome_num = 0
        for c_num in num_c.values():
            current_c_num = c_num // 2 * 2
            if palindrome_num % 2 == 0 and c_num % 2 == 1:
                palindrome_num += 1
            palindrome_num += current_c_num

        return palindrome_num == len(s)