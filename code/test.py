class Solution(object):
    def permutation(self, n):
        if n == 0:
            return 1
        else:
            return n * self.permutation(n - 1)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        base = 1
        p = self.permutation(n - 1)
        '''
        要想解决本题，首先需要了解一个简单的结论：

        对于 n 个不同的元素（例如数 1,2,⋯ ,n），它们可以组成的排列总数目为 n!n!n!。
    
        对于给定的 nn 和 k，我们不妨从左往右确定第 k 个排列中的每一个位置上的元素到底是什么。
        
        我们首先确定排列中的首个元素 a1。根据上述的结论，我们可以知道：
        
            以 1 为 a1​ 的排列一共有 (n−1)!个；
            以 2 为 a1a_1a1​ 的排列一共有 (n−1)!个；
            以 n 为 a1的排列一共有 (n−1)!个。
        
        由于我们需要求出从小到大的第 k 个排列，因此：
    
        如果 k≤(n−1)!，我们就可以确定排列的首个元素为 1；
        如果 (n−1)!<k≤2⋅(n−1)!，我们就可以确定排列的首个元素为 2；
        ⋯
        如果 (n−1)⋅(n−1)!<k≤n⋅(n−1)!，我们就可以确定排列的首个元素为 n。
        '''
        for i in range(n):
            if i * p <= (k - 1) <= (i + 1) * p:
                base = i + 1

        def backtrack(track, choose_list): # 回溯法剪枝，固定第一位，只回溯后几位
            if len(track) == len(choose_list):
                res.append([base] + track[:])

            for choose in choose_list:
                if choose in track:
                    continue

                track.append(choose)
                backtrack(track, choose_list)
                track.pop()

        choose_list = list(range(1, n + 1))
        choose_list.remove(base)
        backtrack([], choose_list)
        final_index = k - (base - 1) * p - 1
        return ''.join(map(str, res[final_index]))

s = Solution()
print(s.getPermutation(3, 3))
print(s.getPermutation(2, 1))
print(s.getPermutation(9, 138270))