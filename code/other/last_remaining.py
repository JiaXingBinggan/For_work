class Solution(object):
    def lastRemaining(self, n, m):
        """
        0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

        例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
        :type n: int
        :type m: int
        :rtype: int
        """
        # 这种模拟方法会超时
        queue = []
        for i in range(n):
            queue.append(i)

        while len(queue) > 1:
            for i in range(m - 1):
                queue.append(queue.pop(0))
                print(queue)

            queue.pop(0)

        return queue[0]

    def lastRemaining1(self, n, m):
        """
        暴力解法，因为是从0开始，设置开始index=0，那么传递m次后则新位置为index + m - 1，此时从0到n-1的数组中去除它（数组长度减一）
        然后新的index仍旧从它开始，然而可能在计算的过程中m比数组的长度大，所以需要对m取余，index = (index + m - 1) % m
        :type n: int
        :type m: int
        :rtype: int
        """
        i, list_n = 0, list(range(n))

        while len(list_n) > 1:
            i = (i + m - 1) % len(list_n)
            list_n.pop(i)

        return list_n[0]

s = Solution()
print(s.lastRemaining(70866, 116922))