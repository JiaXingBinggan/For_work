
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        path = []
        n, m = len(matrix), len(matrix[0])
        l, r, t, b = 0, m - 1, 0, n - 1 # 初始化左、右、上以及下的边界

        while True:
            for i in range(l, r + 1): path.append(matrix[t][i]) # 从左向右，完成后应该上边界下移
            t += 1
            if t > b: break
            for i in range(t, b + 1): path.append(matrix[i][r]) # 从上到下，完成后应该右边界左移
            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1): path.append(matrix[b][i]) # 从右到左，完成后应该下边界上移
            b -= 1
            if b < t: break
            for i in range(b, t - 1, -1): path.append(matrix[i][l]) # 从下到上，完成后应该左边界右移
            l += 1
            if l > r: break
            # 结束后如果还没得到结果，则继续循环

        return path

    def reverseSpiralOrder(self, matrix):
        '''
        逆时针打印
        :param matrix:
        :return:
        '''
        if not matrix:
            return []

        path = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while True:
            for i in range(t, b + 1): path.append(matrix[i][l]) # 从最左边开始右上到下，此时左边界右移
            l += 1
            if l > r: break
            for i in range(l, r + 1): path.append(matrix[b][i]) # 最底层从右到左，此时下边界上移
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1):path.append(matrix[i][r]) # 最右边从下到上，此时右边界左移
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): path.append(matrix[t][i]) # 最上边从右到左，此时上边界下移：
            t += 1
            if t > b: break

        return path


s = Solution()
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(s.reverseSpiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))