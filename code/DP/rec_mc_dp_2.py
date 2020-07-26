class Solution:
    def recMCdp2(self, value_list, change, min_coin, used_coins):
        '''
        找零硬币动态规划解法，其思想为：从最小的change(1)开始，逐步递加，保证每一个change都是最优找零，直到达到change为止
        加入used_coins，用于表示在当前change上使用哪一个类型的硬币
        :param value_list:
        :param change:
        :param min_coin:
        :param used_coins:
        :return:
        '''
        for cents in range(1, change + 1):
            coins = cents # 设置最大值
            new_coin = 1 # 设置当前change使用的新硬币
            for i in [c for c in value_list if c <= cents]:
                if min_coin[cents - i] + 1 < coins:
                    coins = min_coin[cents - i] + 1
                    new_coin = i # 对应最小硬币数的个数
            min_coin[cents] = coins
            used_coins[cents] = new_coin

        self.print_used_coins(used_coins, change)

        return min_coin[change]

    def print_used_coins(self, used_coins, change): # 打印使用的硬币
        while change > 0:
            print(used_coins[change])
            change -= used_coins[change]

s = Solution()
print(s.recMCdp2([1, 5, 10, 21, 25], 45, [0] * 64, [0] * 64))