# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        给定两个二叉树，编写一个函数来检验它们是否相同。
        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not q or not p:
            return False

        pre_p = self.preorder(p)
        pre_q = self.preorder(q)

        return pre_p == pre_q

    def preorder(self, root):
        if not root:
            return ['null']
        else:
            left = self.preorder(root.left)
            right = self.preorder(root.right)

            return [root.val] + left + right