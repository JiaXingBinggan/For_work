# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
                root.right): # 因为要满足任意节点的左右子树的深度相差不超过1，所有需要判断当前root节点的左右子树是否仍旧是平衡二叉树
            return True
        else:
            return False

    def depth(self, root):
        if not root:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1