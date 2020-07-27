from base_data_stracture.graph import Graph

class PriorityQueue:
    '''
    建立一个优先队列，其包括一个顶点和对应点的dist
    '''
    def __init__(self, vertex_list):
        '''
        创建一个二叉堆
        :param vertex_list:
        :return:
        '''
        self.heap_list = [(0, 0)]
        for vertex in vertex_list:
            self.heap_list.append((vertex.getId(), vertex.getDistance())) # 只需要存储其顶点id和distance即可
        self.heap_size = len(vertex_list)

        i = len(vertex_list) // 2 # 从最后一个节点的父节点开始进行下沉操作
        while i > 0:
            self.down(i)
            i -= 1

    def isEmpty(self):
        return self.heap_size == 1

    def delMin(self):
        '''
        返回优先队列中最小distance的节点
        删除节点只需要下沉，只有新增节点才会上浮
        :return:
        '''
        min_vertex = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1] # 用最后一个节点来替换
        self.heap_list.pop() # 移除最后一个
        self.heap_size -= 1
        self.down(1)

        return min_vertex[0]

    def down(self, index):
        '''
        下沉操作
        :param index:
        :return:
        '''
        while (index * 2) <= self.heap_size:
            min_child_index = self.choose_min_child_index(index)
            if self.heap_list[index][1] > self.heap_list[min_child_index][1]:
                temp = self.heap_list[min_child_index]
                self.heap_list[min_child_index] = self.heap_list[index]
                self.heap_list[index] = temp

            index = min_child_index

    def choose_min_child_index(self, index):
        '''
        找出最小子节点的index
        :param index:
        :return:
        '''
        if (2 * index + 1) > self.heap_size:
            return 2 * index # 仅返回左节点
        else:
            if self.heap_list[2 * index][1] > self.heap_list[2 * index + 1][1]:
                return 2 * index + 1
            else:
                return 2 * index

    def rearrangeQueue(self, vertex, new_dist):
        '''
        更新优先队列
        :param vertex:
        :param new_dist:
        :return:
        '''
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.heap_size:
            if self.heap_list[i][0] == vertex.getId():
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heap_list[myKey] = (vertex.getId(), new_dist)
            self.down(1)

    def __contains__(self, vertex):
        for pair in self.heap_list:
            if pair[0] == vertex.getId():
                return True
        else:
            return False

class Dijkstra:
    def dijkstra(self, g, start_vertex_key):
        '''
        Dijkstra算法
        :param g: 图
        :param start_vertex_key: 起始顶点vertex
        :return:
        '''
        for vertex in g:
            vertex.setDistance(1000000)
        g.getVertex(start_vertex_key).setDistance(0)
        priority_queue = PriorityQueue([vertex for vertex in g])

        while not priority_queue.isEmpty():
            current_vertex = g.getVertex(priority_queue.delMin())
            for next_vertex in current_vertex.getConnections():
                new_dist = current_vertex.getDistance() + current_vertex.getWeight(next_vertex)
                if next_vertex.getDistance() > new_dist:
                    next_vertex.setDistance(new_dist)
                    next_vertex.setPred(current_vertex)
                    priority_queue.rearrangeQueue(next_vertex, new_dist)

    def searchMinPath(self, g, start_vertex_key, finish_vertex_key):
        '''
        根据起始节点建立Dijkstra图
        根据结束节点寻找最短路径
        :param g:
        :param start_vertex_key:
        :param finish_vertex_key:
        :return:
        '''
        self.dijkstra(g, start_vertex_key)
        vertex = g.getVertex(finish_vertex_key)

        while vertex.getPred():
            print(vertex.getId())
            vertex = vertex.getPred()
        print(vertex.getId())



g = Graph()
moveTos = [('u', 'x', 1), ('u', 'v', 2), ('u', 'w', 5), ('v', 'w', 3), ('v', 'u', 2), ('v', 'x', 2), ('x', 'u', 1), ('x', 'v', 2), ('x', 'w', 3), ('x', 'y', 1), ('w', 'v', 3), ('w', 'u', 5), ('w', 'x', 3), ('w', 'y', 1), ('w', 'z', 5), ('y', 'x', 1), ('y', 'w', 1), ('y', 'z', 1), ('z', 'w', 5), ('z', 'y', 1)]
for moveTo in moveTos:
    g.addEdge(moveTo[0], moveTo[1], moveTo[2])

d = Dijkstra()
d.searchMinPath(g, 'u', 'w')
print('\n')
d.searchMinPath(g, 'u', 'v')
print('\n')
d.searchMinPath(g, 'u', 'x')
print('\n')
d.searchMinPath(g, 'u', 'y')
print('\n')
d.searchMinPath(g, 'u', 'z')



