from base_data_stracture.dfs_graph import DFSGraph

class Solution:
    def topicalSort(self):
        '''
        拓扑排序：利用DFS算法从工作流中获得最优线性路径
        :return:
        '''
        moveTos = [('3/4 cup milk', '1 cup mix'), ('1 egg', '1 cup mix'), ('1 Tbl Oil', '1 cup mix'), ('1 cup mix', 'heat syrup'), ('1 cup mix', 'pour 1/4 cup'), ('heat griddle', 'pour 1/4 cup'), ('pour 1/4 cup', 'turn when bubbly'), ('turn when bubbly', 'eat'), ('heat syrup', 'eat')] # 工作流有向边
        dfs_graph = DFSGraph()
        for moveTo in moveTos:
            dfs_graph.addEdge(moveTo[0], moveTo[1])

        dfs_graph.dfs()

        vertext_with_finish_time = {}
        for vertex in dfs_graph:
            vertext_with_finish_time[vertex.getId()] = vertex.getFinish()

        sorted_vertext_with_finish_time = sorted(vertext_with_finish_time.items(), key=lambda s: s[1], reverse=True)
        linear_works = []
        for vertex in sorted_vertext_with_finish_time:
            linear_works.append(vertex[0])

        print('->'.join(tuple(linear_works)))

s = Solution()
s.topicalSort()