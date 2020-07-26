from base_data_stracture.graph import Graph
from base_data_stracture.graph import Vertex
from base_data_stracture.queue import Queue

class Solution:
    def wordLabber(self):
        '''
        词梯问题
        :return:
        '''
        g = self.buildGraph()
        self.bfs(g, g.getVertex('FOOL'))

        word = g.getVertex('SAGE')
        pre_word = word
        while pre_word.getPred():
            print(pre_word.getId())
            pre_word = pre_word.getPred()
        print(pre_word.getId())

    def bfs(self, g, start_v):
        '''
        广度优先搜索
        :param g: 图对象
        :param start_v: 起始顶点
        :return:
        '''
        start_v.setColor('gray') # 状态更新为已被发现
        v_queue = Queue() # 创建一个队列用于保存已被发现但未探索完毕的顶点，每遇到一个则放置在队首
        v_queue.enqueue(start_v) # 首先放进起始顶点
        while v_queue.size() > 0: # 直到图中所有顶点都被探索完成
            current_v = v_queue.dequeue() # 拿出队首顶点作为当前节点
            for nbr in current_v.getConnections(): # 遍历当前节点的所有邻接节点
                if nbr.getColor() == 'white': # 非white的可以跳过
                    nbr.setColor('gray') # 更新状态
                    nbr.setDistance(current_v.dist + 1) # 距离起始顶点加1
                    nbr.setPred(current_v) # 设置前驱节点
                    v_queue.enqueue(nbr) # 入队，队列里面的顶点始终是gray的

            current_v.setColor('black') # 遍历完成后，设置状态为探索完成

    def buildGraph(self, wordFile='fourletterwords.txt'):
        '''
        建立4字母单词的桶
        :param wordFile:
        :return:
        '''
        buckets = {} # 建立存放4字母单词的桶，以'_'为通配符
        g = Graph()
        words = open(wordFile, 'r')
        for word in words.readlines():
            current_word = word.strip('\n')
            for i in range(len(current_word)): # 1个word会存在于4个桶内
                bucket = current_word[:i] + '_' + current_word[i+1:] # 以'_'为通配符的桶
                if bucket in buckets: # 如果已有该桶，则直接为该桶新增current_word
                    buckets[bucket].append(current_word)
                else: # 如果没有存储这个桶，则把这个桶的value初始化为一个包含当前word的列表
                    buckets[bucket] = [current_word]

        for bucket in buckets.keys(): # 为桶内每两个word之间新增边,因为里面每个单词之间都只差一个字母
            for word1 in buckets[bucket]:
                for word2 in buckets[bucket]:
                    if word1 != word2: # 如果两者不同则直接添加边
                        g.addEdge(word1, word2) # 增加边的操作

        return g

s = Solution()
s.wordLabber()