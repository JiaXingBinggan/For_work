import sys
class Union:
    def __init__(self, n):
        self.parents = list(range(n)) # 先将每个值的父节点指向自己
        self.ranks = [0 for _ in range(n)]

    def find(self, x):
        root = x
        while root != self.parents[root]: # 找最终的父节点
            root = self.parents[root]
        # 路径压缩
        cur = x
        while cur != root:
            next = self.parents[cur] # 找到当前x的父节点
            self.parents[cur] = root # 将当前x的父节点直接设为root
            cur = next # 继续压缩下一个
        return root # 返回当前x的父节点

    def connect(self, p, q):
        return self.find(p) == self.find((q))

    def union(self, p, q):
        root_p = self.find(p) # 找到p的root
        root_q = self.find(q) # 找到q的root

        if self.ranks[root_p] > self.ranks[root_q]: self.parents[root_q] = root_p
        if self.ranks[root_p] < self.ranks[root_q]: self.parents[root_p] = root_q
        if self.ranks[root_p] == self.ranks[root_q]:
            self.parents[root_p] = root_q
            self.ranks[root_p] += 1

if __name__ == '__main__':
    str1 = sys.stdin.readline().strip()
    test_num = int(str1)
    reses = []
    for _ in range(test_num):
        line_nums = int(sys.stdin.readline().strip())
        lines = []
        for _ in range(line_nums):
            line = list(map(int, sys.stdin.readline().strip().split(' ')))
            if not line:
                break
            lines.append(line)
        # lines = sorted(lines, key=lambda s: s[0])

        visited = set()
        nodes = []
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                if (lines[i][0] <= lines[j][0] <= lines[i][1] and lines[j][1] >= lines[i][1]) or (lines[j][0] <= lines[i][0] <= lines[j][1] and lines[i][1] >= lines[j][1]):
                    nodes.append([i, j])
                    visited.add(i)
                    visited.add(j)

        union = Union(len(visited))

        for node in nodes:
            union.union(node[1], node[0]) # 选择id小的作为父节点

        if len(set(union.parents)) != 1:
            reses.append(False)
        else:
            reses.append(True)
    for res in reses:
        if res:
            print('YES')
        else:
            print('NO')



'''
3
6
9 12
2 11
1 3
6 10
5 7
4 8
5
1 3
2 4
5 9
6 8
7 10
5
5 8
3 6
2 9
7 10
1 4
'''