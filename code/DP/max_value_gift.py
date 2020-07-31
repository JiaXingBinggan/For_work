class Solution(object):
    def maxValue(self, grid):
        """
        在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
        示例 1:
        输入:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        输出: 12
        解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        # 动态规划
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i - 1 < 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j] # 规划方程1
                elif j - 1 < 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j] # 规划方程2
                else:
                    grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) + grid[i][j] # 规划方程3

        return grid[-1][-1]

s = Solution()
print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))