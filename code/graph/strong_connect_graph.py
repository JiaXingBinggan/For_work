from base_data_stracture.dfs_graph import DFSGraph

class Solution:
    def strongConnect(self):
        '''
        利用Kosaraju算法来获取图的强连通分支（一种有向的连通图）
        :return:
        '''
        origin_g = self.buildConnectGraph()
        self.dfs(origin_g, False)
        t_g = self.graphTranposition(origin_g)
        self.dfs(t_g, True)

    def dfs(self, g, is_tranposition):
        '''
        深度遍历算法
        :param g:
        :param is_tranposition: 是否发生了转置
        :return:
        '''
        if not is_tranposition:
            for vertext in g:
                vertext.setColor('white') # 先将所有顶点设为为探索状态
                vertext.setPred(None)

            for vertext in g:
                if vertext.getColor() == 'white':
                    deep_tree = g.dfsvisit(vertext, [])
        else:
            sort_vertexs = []
            for vertex in g:
                sort_vertexs.append([vertex, vertex.getFinish()])

            sort_vertexs = sorted(sort_vertexs, key=lambda s: s[1], reverse=True)

            for vertext in sort_vertexs:
                vertext[0].setColor('white')  # 先将所有顶点设为为探索状态
                vertext[0].setPred(None)

            i = 0
            connect_trees = []
            for vertext in sort_vertexs:
                if vertext[0].getColor() == 'white':
                    deep_tree = g.dfsvisit(vertext[0], [])
                    connect_trees.append(deep_tree)
            print(connect_trees)

    def searchStrongConnect(self, g, start_vertex, connect_s):
        '''
        找到图中的强连通分支
        :param g:
        :param start_vertex:
        :param connect_s: 集合，用于存放连通分支
        :return:
        '''
        if start_vertex.getPred() == None:
            return start_vertex


    def graphTranposition(self, g):
        '''
        图的转置
        :param g: 图
        :return:
        '''
        t_g = DFSGraph()
        for vertex in g: # 遍历原图中每个顶点
            for next_vertex in vertex.getConnections(): # 获取当前顶点的邻接顶点
                    t_g.addEdge(next_vertex.getId(), vertex.getId()) # 转换方向
                    t_g.getVertex(next_vertex.getId()).setFinish(next_vertex.getFinish()) # 将原顶点finish time赋值给转置图对应的点
                    t_g.getVertex(vertex.getId()).setFinish(vertex.getFinish())

        return t_g

    def buildConnectGraph(self):
        '''
        创建连通图
        :return:
        '''
        moveTos = [('A', 'B'), ('B', 'E'), ('B', 'C'), ('C', 'C'), ('C', 'F'), ('D', 'B'), ('D', 'G'), ('E', 'A'), ('E', 'D'), ('F', 'H'), ('G', 'E'), ('H', 'I'), ('I', 'F')]
        connect_graph = DFSGraph()
        for moveTo in moveTos:
            connect_graph.addEdge(moveTo[0], moveTo[1])

        return connect_graph

s = Solution()
s.strongConnect()