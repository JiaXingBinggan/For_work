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
            self.heap_list.append((vertex.getId(), vertex.getDistance()))  # 只需要存储其顶点id和distance即可
        self.heap_size = len(vertex_list)

        i = len(vertex_list) // 2  # 从最后一个节点的父节点开始进行下沉操作
        while i > 0:
            self.down(i)
            i -= 1

    def isEmpty(self):
        return self.heap_size == 1

    def findMin(self):
        '''
        返回最小距离的顶点
        :return:
        '''
        return self.heap_list[1]

    def delMin(self):
        '''
        返回优先队列中最小distance的节点
        删除节点只需要下沉，只有新增节点才会上浮
        :return:
        '''
        min_vertex = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]  # 用最后一个节点来替换
        self.heap_list.pop()  # 移除最后一个
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
            return 2 * index  # 仅返回左节点
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

class Prim:
    def prim(self, g, start_vertex_key):
        '''
        prim算法生成最小生成树
        :param g:
        :param start_vertex_key:
        :return:
        '''
        vertex_list = []
        for vertex in g:
            if vertex.getId() == start_vertex_key:
                vertex.setDistance(0)
            else:
                vertex.setDistance(100000)
            vertex_list.append(vertex)

        priority_queue = PriorityQueue(vertex_list)

        minimum_tree = []
        while not priority_queue.isEmpty():
            current_vertex = g.getVertex(priority_queue.delMin()) # 选择和前驱节点距离最近的顶点（也就是weight最少的顶点）
            for next_vertex in current_vertex.getConnections():
                new_cost = current_vertex.getWeight(next_vertex) # 获取当前节点current_vertex到它的邻接节点的距离
                print(new_cost)
                if next_vertex in priority_queue and new_cost < next_vertex.getDistance(): # 选择可以安全添加的边，也就是不在树中的边；并且weight最小的边（这里的new_cost<next_vertex.getDistance()的目的为将边的边长更新为weight，以便于选出下一个具有最小边长的顶点。因为还没探索到的边的边长都是最大值）
                    next_vertex.setDistance(new_cost)
                    next_vertex.setPred(current_vertex) # 前驱节点设为当前节点
                    priority_queue.rearrangeQueue(next_vertex, new_cost) # 因为更新了距离，所以需要更新优先队列，以选出下一个具有最小边长的顶点
            next_min_dist_v = priority_queue.findMin()
            min_edge = [g.getVertex(next_min_dist_v[0]).getPred().getId(), next_min_dist_v[0], next_min_dist_v[1]]
            minimum_tree.append(min_edge)

        return minimum_tree

g = Graph()
moveTos = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 1), ('B', 'E', 4), ('C', 'F', 5), ('D', 'E', 1), ('E', 'F', 1), ('F', 'G', 1)]
reverseMoveTos = []
for moveTo in moveTos:
    reverseMoveTos.append((moveTo[1], moveTo[0], moveTo[2]))
moveTos.extend(reverseMoveTos)

for moveTo in moveTos:
    g.addEdge(moveTo[0], moveTo[1], moveTo[2])

p = Prim()
print(p.prim(g, 'A'))




