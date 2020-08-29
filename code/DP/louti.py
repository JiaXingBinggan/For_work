#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param n int整型 正整数n,表示有n个台阶要走，可以爬6,5,4,3,2,1个楼梯
# @return int整型
#
class Solution:
    def ClimbStairs(self, n):
        # write code here+
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if i < 6:
                for j in range(i - 1, -1, -1):
                    dp[i] += dp[j]
            else:
                for j in range(1, 7):
                    dp[i] += dp[i - j]

        return dp[n]

s = Solution()
print(s.ClimbStairs(5))