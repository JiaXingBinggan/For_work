class Solution(object):
    def longestPalindrome(self, s):
        """
        给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

        在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

        输入:
        "abccccdd"

        输出:
        7

        解释:
        我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        num_c = {}
        for c in s:
            if c not in num_c:
                num_c.setdefault(c, 1)
            else:
                num_c[c] += 1

        palinrome_num = 0
        for c_num in num_c.values():
            current_num = c_num // 2 * 2  # 不管是偶数还是奇数，最后都只取偶数个值，例如某个字符的长度为4则肯定取4，如果长度为5则同样取4
            if palinrome_num % 2 == 0 and c_num % 2 == 1:  # 遇到第一个为奇数个数字符时，则首先加1（因为奇数字符至少取1个）。因为遇到第一个奇数字符之前palinrome都是偶数，加上1后就变成了奇数
                palinrome_num += 1
            palinrome_num += current_num  # 这个是为了加上剩下的比例，假设奇数字符的长度为1，则current_num=0；如果长度为3时，则current_num=2。而前面已经加了1了所以后都只用添加current_num即可

        return palinrome_num