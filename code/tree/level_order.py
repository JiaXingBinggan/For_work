class Solution(object):
    def levelOrder(self, root):
        """
        从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
        例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7

        返回：

        [3,9,20,15,7]
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: # 一定要记住边界条件
            return []

        queue = [root]
        res = [root.val]
        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.left:
                res.append(current_node.left.val)
                queue.append(current_node.left)

            if current_node.right:
                res.append(current_node.right.val)
                queue.append(current_node.right)

        return res