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
    line = list(map(int, input().split(' ')))
    n, m = line[0], line[1]

    order_list = []
    union = Union(n)
    for i in range(m):
        same_xiaoqu = list(map(int, input().split(' ')))
        union.union(same_xiaoqu[0] - 1, same_xiaoqu[1] - 1)
    orders = []
    for order in set(union.parents):
        current_orders = []
        for i, parent in enumerate(union.parents):
            if parent == order:
                current_orders.append(str(i + 1))
        orders.append(sorted(current_orders))
    orders = sorted(orders, key=lambda s: s[0])

    print(len(orders))
    for order in orders:
        print(' '.join(tuple(order)))


