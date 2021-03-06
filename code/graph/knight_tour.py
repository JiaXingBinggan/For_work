from base_data_stracture.graph import Graph

class Solution:
    def knightTour(self, board_size=5):
        '''
        骑士周游问题
        :return:
        '''
        knight_graph = self.buildKnightGraph(board_size)
        path = []
        self.dfs(1, path, knight_graph.getVertex((0,0)), board_size * board_size - 1) # 层次要从1开始，因为第一个点已经在路径中了

        path_len = len(path)
        while len(path) > 0:
            vertex = path.pop()
            print(vertex.getId())

        return path_len

    def buildKnightGraph(self, boardSize):
        '''
        创建骑士周游图
        :param boardSize:
        :return:
        '''
        knight_graph = Graph()
        for row in range(boardSize): # 行
            for col in range(boardSize): # 列
                current_legal_move_tos = self.getLegalMoveTos(row, col, boardSize) # (row, col)为当前位置坐标
                for move_to in current_legal_move_tos:
                    knight_graph.addEdge((row, col), move_to) # 新增一条边，由坐标到坐标

        return knight_graph

    def dfs(self, n, path, u, limit):
        '''
        深度优先搜索
        :param n: 当前层次
        :param path: 存放路径（一般用栈实现，也可以直接用list，但需要保持栈先进后出的性质）
        :param u: 当前节点
        :param limit: 路径长度=boarSize*boarSize - 1
        :return:
        '''
        u.setColor('gray') # 当前节点已被探索到
        path.append(u) # 路径栈
        if n < limit: # 当层次没有达到limit时，需要不断深入（遍历）
            connect_list = list(u.getConnections()) # 获取当前节点的邻接节点
            # 该步骤可以用Warnsdorff算法优化
            i = 0
            done = False
            while i < len(connect_list) and not done: #
                if connect_list[i].getColor() == 'white': # 当存在可进一步更深地探索的顶点时
                    done = self.dfs(n + 1, path, connect_list[i], limit) # 继续往更深的地方遍历
                i = i + 1
            if not done: # 如果当前节点已经走不通了，则退回上一层，继续遍历其兄弟即诶但
                path.pop() # 在路径中去除栈顶顶点
                u.setColor('white') # 退回为未改变的样子
        else:
            done = True

        return done

    def getLegalMoveTos(self, x, y, boardSize):
        '''
        将boadrSize*boardSize的棋盘认做一个坐标轴，获取每一个棋盘格(x,y)的合法移动位置列表
        :param x:
        :param y:
        :param boardSize:
        :return:
        '''
        legalMoveTos = []
        availableMoves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)] # 最多可能可以移动的方向
        for move in availableMoves:
            new_x = x + move[0]
            new_y = y + move[1]
            if self.isLegalMove(new_x, boardSize) and self.isLegalMove(new_y, boardSize): # 如果均合法，则添加其移动后的位置
                legalMoveTos.append((new_x, new_y))

        return legalMoveTos

    def isLegalMove(self, x, boardSize):
        '''
        判断移动后的棋盘格是否合法，不能小于0，不能大于boardSize
        :param x:
        :param boardSize:
        :return:
        '''
        if x >= 0 and x < boardSize: # 因为标记是从0开始，所有直接小于boarSize即可
            return True
        else:
            return False

s = Solution()
print(s.knightTour(3))