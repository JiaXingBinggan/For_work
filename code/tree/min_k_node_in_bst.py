# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0

        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right