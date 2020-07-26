class Solution:
    def thief(self, max_w):
        '''
        博物馆大盗问题：动态规划解法
        :param tr: weight-value集合
        :param max_w: 最大负重
        :return: 能够得到的最多价值
        '''
        tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]

        # 初始化m(i, w)
        m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

        # 动态规划解法
        for i in range(1, len(tr)):
            for w in range(max_w + 1):
                if tr[i]['w'] > w: # 也就是第i件宝物对新增没有任何意义，因为本身weight都大于w了
                    m[(i, w)] = m[(i - 1, w)]
                else:
                    m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])
                    # 也就是第i件，选或不选两种情况，对于选就需要退回第i - 1件之前的情况，也就是m(i - 1, w - wi)，
                    # 因为没选时，是没有加上wi的重量的
        
        return m[(5, 20)]

s = Solution()
print(s.thief(20))