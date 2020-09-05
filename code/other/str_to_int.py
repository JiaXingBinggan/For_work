class Solution(object):
    def strToInt(self, str_):
        """
        写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
        https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
        :type str: str
        :rtype: int
        """
        # 这个题就是有很多边界条件一定要注意提前思考清楚
        if not str_: # 字符串本身为空
            return 0

        i = 0
        while str_[i] == ' ':
            i += 1
            if i == len(str_): return 0 # 字符串只包含了空格

        is_neg = 1
        if str_[i] == '-':
            is_neg = -1
            i += 1
        elif str_[i] == '+':
            i += 1
        elif str_[i] not in '0123456789': # 如果去除空格后，一来遇到的不是数字，则直接返回0
            return 0

        temp_num_str = ''
        while i < len(str_) and str_[i] in '0123456789':
            temp_num_str += str_[i]
            i += 1

        int_min, int_max = -2 ** 31, 2 ** 31 - 1

        return_int = 0
        for i, c in enumerate(temp_num_str):
            return_int += (ord(c) - ord('0')) * (10 ** (len(temp_num_str) - i - 1)) # 字符串转换数字
        return_int = return_int * is_neg

        if return_int > int_max: # 数字太大
            return int_max

        if return_int < int_min: # 数字太小
            return int_min

        return return_int


