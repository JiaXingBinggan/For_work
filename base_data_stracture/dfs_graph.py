from base_data_stracture.graph import Graph

class DFSGraph(Graph): # 继承Graph
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertext in self:
            vertext.setColor('white') # 先将所有顶点设为为探索状态
            vertext.setPred(None)

        for vertex in self:
            if vertex.getColor() == 'white': # 如果存在还未发现的顶点，则建立深度优先森林
                self.dfsvisit(vertex)

    def dfsvisit(self, start_vertext, deep_tree):
        '''
        深度优先遍历
        :param start_vertext: 起始（递归中为当前）顶点
        :param deep_tree: 当前深度优先树
        :return:
        '''
        deep_tree.append(start_vertext.getId())
        start_vertext.setColor('gray') # 首先要把其设为被发现
        self.time += 1
        start_vertext.setDiscover(self.time) # 记录当前节点被发现的时间
        for c_vertex in start_vertext.getConnections():
            if c_vertex.getColor() == 'white':
                c_vertex.setPred(start_vertext)
                self.dfsvisit(c_vertex, deep_tree) # 继续递归往深度遍历
        start_vertext.setColor('black') # 当前节点没有邻接顶点，或者其它邻接节点均已被发现或完成探索，则当前节点完成探索
        self.time += 1
        start_vertext.setFinish(self.time)

        return deep_tree