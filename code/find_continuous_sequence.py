class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        choose_num = list(range(1, target))
        dp = [[0]] * len(choose_num)
        dp[0] = [choose_num[0]]

        for i in range(1, len(choose_num)):
            dp[i] = dp[i - 1] + [choose_num[i]]
            while sum(dp[i]) > target:
                dp[i].pop(0)

        res = []
        for item in dp:
            if sum(item) == target:
                res.append(item)

        return res

    def findContinuousSequence2(self, target):
        '''
        间隔法：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/xiang-jie-hua-dong-chuang-kou-fa-qiu-gen-fa-jian-g/
        :param target:
        :return:
        '''
        # 我们的间隔从1开始
        i, res = 1, []

        # 根据上面的条件1，限定i的大小，即间隔的范围
        while i * (i + 1) / 2 < target:
            # 根据条件2，如果x不为整数则扩大间隔
            if not (target - i * (i + 1) / 2) % (i + 1):
                # 如果两个条件都满足，代入公式求出x即可，地板除//会把数改成float形式，用int()改回来
                x = int((target - i * (i + 1) / 2) // (i + 1))
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x, x + i + 1)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]


s = Solution()
print(s.findContinuousSequence(15))