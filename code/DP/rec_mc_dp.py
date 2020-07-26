class Solution:
    def recMCdp(self, value_list, change, min_coins):
        '''
        找零硬币动态规划解法，其思想为：从最小的change(1)开始，逐步递加，保证每一个change都是最优找零，直到达到change为止
        :param value_list:
        :param change:
        :param min_coins: change的最优找零list，长度为change + 1
        :return: min_coins[change]
        '''
        for cents in range(1, change + 1):
            coins = cents # 设置最多coin，也就是全部都用1分找零
            for i in [c for c in value_list if c <= cents]: # 过滤条件，例如当cents为1，根本不需要用到5，10，25这三种硬币
                if min_coins[cents - i] + 1 < coins:
                    coins = min_coins[cents - i] + 1
            min_coins[cents] = coins
        print(min_coins)
        return min_coins[change]

s = Solution()
print(s.recMCdp([1, 5, 10, 25], 63, [0] * 64))