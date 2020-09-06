class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        first, second, third = 1, 2, 4
        res = 0
        for i in range(4, n + 1):
            res = (first + second + third) % (10 ** 9 + 7) # 要记得取余
            first, second, third = second, third, res

        return res % (10 ** 9 + 7) # 要记得取余