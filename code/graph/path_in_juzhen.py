class Solution(object):
    def exist(self, board, word):
        """
        https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k): # dfs用于寻找路径标准写法（加剪枝）
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp # 记得这里要还原
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
