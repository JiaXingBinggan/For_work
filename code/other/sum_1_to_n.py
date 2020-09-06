class Solution(object):
    def __init__(self):
        self.sum_ = 0

    def sumNums(self, n):
        """
        求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
        :type n: int
        :rtype: int
        """
        # if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false
        # if(A || B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true
        n > 1 and self.sumNums(n - 1) # 用短路来实现
        self.sum_ += n

        return self.sum_

    def sum_nums(self, n):
        return n > 1 and n + self.sumNums(n - 1)

s = Solution()
# print(s.sumNums(9))
print(s.sum_nums(9))