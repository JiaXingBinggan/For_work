class Solution(object):
    def movingCount(self, m, n, k):
        """
        地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        queue, visited = [(0, 0, 0, 0)], set()

        while len(queue) > 0:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or si + sj > k or (i, j) in visited:
                continue

            visited.add((i, j))
            queue.append([i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj])
            queue.append([i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8])

        return len(visited)