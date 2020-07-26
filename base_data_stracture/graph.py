class Vertex: # 图顶点类
    def __init__(self, key):
        '''
        初始化
        :param key: 顶点id的值
        '''
        self.id = key
        self.connectedTo = {} # 该顶点所连接的顶点集合
        self.color = 'white' # white表示未被发现，gray表示已被发现（但其没有遍历完其所有的邻接顶点），black表示已探索完所有其邻接顶点
        self.dist = 0 # 表示当前顶点到起始顶点的距离
        self.pred = None # 表示当前节点的前驱节点
        self.discover = 0 # 当前节点被初次发现时间（用于深度优先搜索）
        self.finish = 0 # 当前节点完成探索时间（用于深度优先搜索）

    def setColor(self, color):
        '''
        设置当前节点状态
        :param color: white、gray、black
        :return:
        '''
        self.color = color

    def getColor(self):
        return self.color # 返回当前状态

    def setDistance(self, dist):
        '''
        设置当前节点到起始顶点的距离
        :param dist:
        :return:
        '''
        self.dist = dist

    def getDistance(self):
        return self.dist # 返回其到起始顶点的距离

    def setPred(self, vertex):
        '''
        设置其前驱节点
        :param vertex:
        :return:
        '''
        self.pred = vertex

    def getPred(self):
        return self.pred # 返回其前驱节点

    def setDiscover(self, time):
        '''
        设置节点被发现时间
        :param time: 当前时间
        :return:
        '''
        self.discover = time

    def getDiscover(self):
        return self.discover # 返回被发现时间

    def setFinish(self, time):
        '''
        设置节点完成探索的时间，也就是其没有其它邻接顶点
        :param time:
        :return:
        '''
        self.finish = time

    def getFinish(self):
        return self.finish # 返回探索完成时的时间

    def addNeighbor(self, nbr, weight=0):
        '''
        为当前顶点增加一个邻接节点
        :param nbr: 邻接节点（同样是Vertex类）
        :param weight:
        :return:
        '''
        self.connectedTo[nbr] = weight

    def getConnections(self):
        '''
        返回所有邻接顶点
        :return:
        '''
        return self.connectedTo.keys()

    def getId(self):
        '''
        返回当前顶点的id
        :return:
        '''
        return self.id

    def getWeight(self, nbr):
        '''
        返回当前顶点与邻接顶点nbr的边的weight
        :param nbr:
        :return:
        '''
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertexList = {} # 所有顶点列表
        self.numVertexs = 0 # 顶点个数

    def addVertex(self, key):
        '''
        为图新增一个顶点
        :param key: 顶点id的值
        :return:
        '''
        self.numVertexs += 1
        new_vertex = Vertex(key)
        self.vertexList[key] = new_vertex

        return new_vertex

    def getVertex(self, key):
        '''
        返回图中的顶点
        :param key:
        :return:
        '''
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None # 如果没有，直接返回None

    def __contains__(self, item):
        return item in self.vertexList # 判断是否某个顶点在图中

    def addEdge(self, fromKey, toKey, weight=0):
        '''
        为两个顶点新增一条边
        :param fromKey: 起始顶点
        :param toKey: 终止顶点
        :param weight:
        :return:
        '''
        if fromKey not in self.vertexList: # 如果图中不存在该点，则必须
            new_fromV = Vertex(fromKey)
            self.vertexList[fromKey] = new_fromV
        if toKey not in self.vertexList:
            new_toV = Vertex(toKey)
            self.vertexList[toKey] = new_toV
        self.vertexList[fromKey].addNeighbor(self.vertexList[toKey], weight) # 新增边本质是指：对某个点新增一个邻接顶点

    def getVertexs(self):
        '''
        返回所有的顶点id
        :return:
        '''
        return self.vertexList.keys()

    def __iter__(self):
        '''
        为了能够迭代取出图中的顶点对象
        :return:
        '''
        return iter(self.vertexList.values())