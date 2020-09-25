'''
很多同学都知道，求解一个数字的所有因子，使用 O(sqrt(n)) 的时间就可以。

这是因为，当我们知道 d 是 n 的因子的时候，就知道了 n / d 也是 n 的因子。所以，我们只需要从 1 搜索到 sqrt(n) 就足够了。

但是因为这个问题最后要将所有因子按照升序排列，因此，以下代码虽然在 O(sqrt(n)) 的时间里完成了查找 n 的所有因子，但最终排序反而让复杂度升高了。
因此两边往中间靠拢即可
'''
class Solution:
    def Factor(self, n):
        forward = []
        backward = []

        middle = int(n**0.5)
        for i in range(1,middle+1):
            if n % i == 0:
                forward.append(i)
                if i == int(n/i):
                    break
                backward.append(int(n/i))

        return forward + backward[::-1]

s = Solution()
print(s.Factor(16))