import time
class Solution:
    def recMC2(self, value_list, change, knowed_list):
        '''
        对recMC的改进，存储中间结果以减少重复计算
        :param value_list:
        :param change:
        :param knowed_list, 用于存储中间结果，其长度跟change有关，len = change + 1
        :return:
        '''
        min_coins = change
        if change in value_list: # 递归基本结束条件
            knowed_list[change] = 1
            return 1
        elif knowed_list[change] > 0:
            return knowed_list[change] # 如果已经计算过当前change的最优找零，则直接返回，省去重复计算
        else:
            for i in [c for c in value_list if c < change]:
                num_coins = 1 + self.recMC2(value_list, change - i, knowed_list)
                if num_coins < min_coins:
                    min_coins = num_coins
                    knowed_list[change] = min_coins # 替换当前change的最优找零

        return min_coins

s = Solution()
print(time.clock())
print(s.recMC2([1, 5, 10, 25], 63, [0] * 64))
print(time.clock())