# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        给定一个二叉树，检查它是否是镜像对称的。
        例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

            1
           / \
          2   2
         / \ / \
        3  4 4  3



        但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

            1
           / \
          2   2
           \   \
           3    3
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.recur(root.left, root.right)

    def recur(self, left, right):
        if not left and not right: # 如果没有子节点了是对称的
            return True
        elif left and right: # 如果左右子节点均有
            if left.val == right.val:
                return self.recur(left.left, right.right) and self.recur(left.right, right.left)
            # 则只有到左子树的左节点和右子树的右节点相同；或者左子树的右节点和右子树的左节点相同才算对称。
            else:
                return False
        else:
            return False

