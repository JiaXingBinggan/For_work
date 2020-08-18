class Solution(object):
    def pathSum_backtrack(self, root, sum_):
        if not root:
            return []
        res, path = [], []
        def backtrack(root, sum_):
            path.append(root.val)
            sum_ -= root.val
            if sum_ == 0 and not root.left and not root.right:
                res.append(list(path)) # 这里需要使用list(path)重新生成一个复制；否则因为path是相对于backtrack函数的全局变量，会不断变化
            backtrack(root.left, sum_)
            backtrack(root.right, sum_)
            path.pop()

        backtrack(root, sum_)

        return res

    def pathSum_backtrack_2(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []

        def backtrack(track, root): # 通用模板的方法
            if sum(track) == sum_ and not root.left and not root.right:
                res.append(track[:])

            if root.left: # chooselist来自root
                track.append(root.left.val)
                backtrack(track, root.left)
                track.pop()

            if root.right:
                track.append(root.right.val)
                backtrack(track, root.right)
                track.pop()

        backtrack([root.val], root)

        return res

    def pathSum_dfs(self, root, sum_):
        if not root:
            return []
        stack = [(root, [root.val])] # dfs记录了每一条路径
        res = []
        while stack:
            current_n, current_path = stack.pop()
            if sum(current_path) == sum_ and not current_n.left and not current_n.right:
                res.append(current_path)
            if current_n.left:
                stack.append((current_n.left, current_path + [current_n.left.val]))
            if current_n.right:
                stack.append((current_n.right, current_path + [current_n.right.val]))

        return res

    def pathSum_bfs(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, [root.val])]
        res = []
        while queue:
            current_root, current_path = queue.pop(0)
            if sum(current_path) == sum_ and not current_root.left and not current_root.right:
                res.append(current_path)
            if current_root.left:
                queue.append((current_root.left, current_path + [current_root.left.val]))
            if current_root.right:
                queue.append((current_root.right, current_path + [current_root.right.val]))

        return res
