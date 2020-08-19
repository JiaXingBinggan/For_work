class Solution(object):
    def translateNum(self, num):
        """
        给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
        :type num: int
        :rtype: int
        """
        if num < 10:
            return 1

        str_num = str(num)
        dp = [0] * len(str_num)
        dp[0] = 1

        if int(str_num[0] + str_num[1]) > 25:
            dp[1] = 1
        else:
            dp[1] = 2

        for i in range(2, len(str_num)):
            if 10 <= int(str_num[i - 1] + str_num[i]) <= 25:  # 因为可能存在509的情况，
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]