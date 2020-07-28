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

s = Solution()
print(s.lastRemaining(70866, 116922))