class Solution(object):
    def numIslands(self, grid):
        """
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

        岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

        此外，你可以假设该网格的四条边均被水包围。



        示例 1:

        输入:
        [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
        ]
        输出: 1

        示例 2:

        输入:
        [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
        ]
        输出: 3
        解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])

        count = 0
        v_queue = []
        move_tos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                else:
                    continue
                v_queue.append((i, j))
                while len(v_queue) > 0:
                    current_node = v_queue.pop(0)
                    for move in move_tos:
                        next_move = (move[0] + current_node[0], move[1] + current_node[1])
                        if 0 <= next_move[0] < n and 0 <= next_move[1] < m and\
                                        grid[next_move[0]][next_move[1]] == '1':
                            grid[next_move[0]][next_move[1]] = '0'
                            v_queue.append(next_move)
        return count

s = Solution()
print(s.numIslands([
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]))
print(s.numIslands([
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]))
print(s.numIslands([["0","1","0"],["1","0","1"],["0","1","0"]]))