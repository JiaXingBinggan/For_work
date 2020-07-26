import time
class Solution:
    def recMC(self, value_list, change):
        '''
        :param value_list: 硬币体系值，例如[1, 5, 10, 25]
        :param change: 需要找零的零钱数量
        :return: 最少的硬币个数
        '''
        min_coins = change # 初始化最少硬币数为change
        if change in value_list:
            return 1 # 如果刚好剩余零钱直接可以找零，即返回1
        else:
            for i in [c for c in value_list if c < change]: # 设置一个过滤条件，例如当change小于25时，就没必要再对value_list所有值进行循环
                num_coins = 1 + self.recMC(value_list, change - i) # 递归，除去当前找零值后进行递归
                if num_coins < min_coins:
                    min_coins = num_coins

        return min_coins

s = Solution()
'''
该递归算法低效，递归时间太长
'''
print(time.clock())
print(s.recMC([1, 5, 10, 25], 63))
print(time.clock())