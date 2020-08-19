"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        def inorder(root):
            if not root:
                return []
            else:
                left = inorder(root.left)
                right = inorder(root.right)

                return left + [root] + right

        inorder_arr = inorder(root)
        if len(inorder_arr) == 1:
            root.left = root
            root.right = root
            return root

        for i in range(len(inorder_arr)):
            node = inorder_arr[i]
            if i == 0:
                node.left = inorder_arr[-1]
                node.right = inorder_arr[1]
            elif i == len(inorder_arr) - 1:
                node.left = inorder_arr[i - 1]
                node.right = inorder_arr[0]
            else:
                node.left = inorder_arr[i - 1]
                node.right = inorder_arr[i + 1]

        return inorder_arr[0]

