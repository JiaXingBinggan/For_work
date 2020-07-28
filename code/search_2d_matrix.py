class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])

        i, j = n - 1, 0 # 左下角标志法：因为每一行从左到右递增，每一列从上到下递增，所以当当前位置的数大了，则往上移动一行；当当前位置的数小了，则往右移动一列

        is_exist = False
        while i >= 0 and j < m:

            if matrix[i][j] == target:
                is_exist = True
                break
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1

        return is_exist

s = Solution()
# print(s.findNumberIn2DArray([
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ], 20))
print(s.findNumberIn2DArray([[-5]], -5))