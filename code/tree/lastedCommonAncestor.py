# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        '''
       最近公共祖先的定义： 设节点 root为节点 p,q的某公共祖先，若其左子节点 root.left和右子节点 root.right都不是 p,qp,qp,q 的公共祖先，则称 root是 “最近的公共祖先” 。

根据以上定义，若 root是 p,q的 最近公共祖先 ，则只可能为以下情况之一：

    p和 q在 root的子树中，且分列 root的 异侧（即分别在左、右子树中）；
    p=root，且 q在 root的左或右子树中；
    q=root，且 p在 root的左或右子树中
       '''
        if not root:  # 为空也直接返回
            return root
        if root == p or root == q:  # 如果根节点等于p或者q则直接返回
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 遍历左子树
        right = self.lowestCommonAncestor(root.right, p, q)  # 遍历右子树

        if not left and not right:  # 当左右子树都没有p或者q时，返回null
            return
        if not left:  # 如果左子树不存在p或者q时，直接返回右子树
            return right
        if not right:  # 如果右子树不存在p或者q时，直接返回左子树
            return left

        return root  # 当左右子树都存在p或者q时，则root为最近公共祖先