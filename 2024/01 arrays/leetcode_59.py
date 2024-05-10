"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]

提示：

1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 0:
            return []

        left, right, top, bottom = 0, n - 1, 0, n - 1

        res = [n * [0] for _ in range(n)]

        num = 1

        while left <= right and top <= bottom:
            # 从左到右，结束后下移一行
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1

            # 从上到下，结束后向左一列
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            # 从右到左，结束后上移一行
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = num
                    num += 1
            bottom -= 1

            # 从下到上，结束后向右一列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res[i][left] = num
                    num += 1
            left += 1

        return res


s = Solution()
print(s.generateMatrix(3))