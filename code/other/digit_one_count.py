class Solution(object):
    def countDigitOne(self, n):
        """
        输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
        :type n: int
        :rtype: int
        """
        num_1_times = 0
        for n in range(n + 1):
            str_n = str(n)
            if '1' in str(str_n):
                i = 0
                while i < len(str_n):
                    if '1' == str_n[i]:
                        num_1_times += 1
                    i += 1
            else:
                continue

        return num_1_times

s = Solution()
print(s.countDigitOne(824883294))