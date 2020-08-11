# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        二叉搜索树中的两个节点被错误地交换。
        请在不改变其结构的情况下，恢复这棵树。
        https://leetcode-cn.com/problems/recover-binary-search-tree/
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        inorder_root_arr = self.inorder(root)
        sort_root_arr = sorted(inorder_root_arr, key=lambda s: s.val)
        temp = [inorder_root_arr[i] for i in range(len(inorder_root_arr)) if inorder_root_arr[i] != sort_root_arr[i]]
        temp[0].val, temp[1].val = temp[1].val, temp[0].val

        return root

    def inorder(self, root):
        if not root:
            return []
        else:
            left = self.inorder(root.left)
            right = self.inorder(root.right)

            return left + [root] + right