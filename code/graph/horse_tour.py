from base_data_stracture.graph import Graph

class Solution:
    def horseTour(self, n, m, x, y):
        '''
        有一个n*m的棋盘(1< n,m<=400)，在某个点上有一个马,要求你计算出马到达棋盘上任意一个点(x, y)最少要走几步
        :return:
        '''
        horse_graph = self.horseGraph(n, m)
        self.bfs(horse_graph, horse_graph.getVertex((x, y)))

        horse_dists = []
        for col in range(m - 1, -1, -1):
            row_dists = []
            for row in range(n):
                row_dists.append(horse_graph.getVertex((row, col)).getDistance())
                # print(horse_graph.getVertex((row, col)).getDistance())
            horse_dists.append(row_dists)

        for horse_dist in horse_dists:
            print(' '.join(tuple([str(dist) for dist in horse_dist])))

    def bfs(self, g, first_v):
        '''
        广度优先遍历
        :param g:
        :param first_v: 起始顶点
        :return:
        '''
        first_v.setColor('gray')
        v_queue = [] # 顶点序列
        v_queue.append(first_v)

        while len(v_queue) > 0:
            current_v = v_queue.pop(0) # 队列先进先出
            for nbr in current_v.getConnections(): # 遍历所有邻接顶点
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                    nbr.setPred(current_v)
                    nbr.setDistance(current_v.dist + 1) # 前驱节点距离加1
                    v_queue.append(nbr)

            current_v.setColor('black')

    def horseGraph(self, boardSize_n, boardSize_m):
        '''
        创建马的遍历的树
        :param boardSize_n:
        :param boardSize_m:
        :return:
        '''
        horse_graph = Graph()
        for row in range(boardSize_n):
            for col in range(boardSize_m):
                current_move_tos = self.getLegalMoveTos(row, col, boardSize_n, boardSize_m)
                for move_to in current_move_tos:
                    horse_graph.addEdge((row, col), move_to)

        return horse_graph

    def getLegalMoveTos(self, x, y, boardSize_n, boardSize_m):
        '''
        获取当前坐标，能够移动的合法坐标
        :param x:
        :param y:
        :param boardSize_n:
        :param boardSize_m:
        :return:
        '''
        moveTos = []
        availableMoves = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        for move in availableMoves:
            new_x = x + move[0]
            new_y = y + move[1]
            if self.isLegalMove(new_x, boardSize_n) and self.isLegalMove(new_y, boardSize_m):
                moveTos.append((new_x, new_y))

        return moveTos

    def isLegalMove(self, x, boardSize):
        if x >= 0 and x < boardSize:
            return True
        else:
            return False

s = Solution()
s.horseTour(11, 8, 1, 1)