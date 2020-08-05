'''
无向图
A----------B-----------------D---------------F
 -        -                - -
  -      -          -        -
    -   -     -              -
       -C--------------------E

'''
# 邻接矩阵
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'D', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

def DFS(graph, start): # DFS 用栈
    v_stack = [] # 存放顶点的栈，栈有先进后出的特性
    v_stack.append(start) # 起始节点入栈
    visited = set() # 用于存放已被观测到的顶点
    visited.add(start) # 首先把起始节点设为已被观测到

    while len(v_stack) > 0:
        current_v = v_stack.pop() # 先进后出
        nbr_vs = graph[current_v] # 获取当前节点的邻接顶点
        for nbr_v in nbr_vs:
            if nbr_v not in visited:
                v_stack.append(nbr_v) # 当存在没被遍历到的节点，则直接放入栈顶（因为出栈时都是从最后一个出）
                visited.add(nbr_v)
        print(current_v)

def BFS(graph, start): # BFS用队列
    v_queue = [] # 存放顶点的队列，队列有先进先出的特性
    v_queue.append(start)
    visited = set() # 同样适用
    visited.add(start)

    while len(v_queue) > 0:
        current_v = v_queue.pop(0) # 先进先出
        nbr_vs = graph[current_v]
        for nbr_v in nbr_vs:
            if nbr_v not in visited:
                v_queue.append(nbr_v)
                visited.add(nbr_v)

        print(current_v)

DFS(graph, "A")
print("-----------")
BFS(graph, "B")