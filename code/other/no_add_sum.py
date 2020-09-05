class Solution(object):
    def add(self, a, b):
        """
        写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x # 求补码的操作（按位与）
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & x  # 异或^计算不进位的和，与&计算进位（要向左移动一位）

        return a if a <= 0x7fffffff else ~(
                    a ^ x)  # 若补码 aaa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式


