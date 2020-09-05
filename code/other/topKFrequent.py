class Solution:
    def topKFrequence(self, lst, k):
        '''
        给定一个列表与数字K，按出现次数倒序输出列表中前K个出现最频繁的元素；若少于K个元素则返回所有元素
        :param lst:
        :param k:
        :return:
        '''
        if len(lst) <= k:
            return set(lst)

        fre_dict = {}

        for num in lst:
            if num not in fre_dict.keys():
                fre_dict.setdefault(num, 1)
            else:
                fre_dict[num] += 1

        sorted_fre_dict = sorted(fre_dict.items(), key = lambda s: s[1], reverse=True) # dict.items会返回一个列表，列表内包含着各个key-value键值对（以元组呈现）例如[(1, 3), (2, 2), (3, 1)]

        top_k = []
        for tp in sorted_fre_dict[:k]:
            top_k.append(tp[0])

        return top_k

s = Solution()
print(s.topKFrequence([1,1,1,2,2,3], 2))
