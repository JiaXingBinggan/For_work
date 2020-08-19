"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node.children)) # 要node.children

        return res

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        for node in root.children:
            res.extend(self.postorder(node)) # 注意和前面的区别
        res.extend([root.val])

        return res

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        n_queue = [root]
        res = []

        while len(n_queue) >= 1:
            current_res = []
            for _ in range(len(n_queue)): # 注意是一层接一层地遍历
                current_n = n_queue.pop(0)
                current_res.append(current_n.val)
                n_queue.extend(current_n.children)
            res.append(current_res)

        return res

    def maxDepth(self, root):
        """
        N叉树的最深深度
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            children_depth = []
            for node in root.children:
                children_depth.append(self.maxDepth(node))
        return max(children_depth) + 1