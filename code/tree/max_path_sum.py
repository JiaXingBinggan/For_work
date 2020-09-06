# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型
#

'''
题目描述
给定一个二叉树，请计算节点值之和最大的路径的节点值之和是多少。
这个路径的开始节点和结束节点可以是二叉树中的任意节点
例如：
给出以下的二叉树，

返回的结果为6
示例1
输入
{-2,1}

输出
1
'''

'''
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

我们先定义一个全局变量res=flaot("-inf")来存储全局的最大值，也就是我们需要返回的值

对于节点值为20的节点，我们考虑的是对于以这个节点为根节点的路径的最大值是多少

我们有这么几种几种情况:

1.根节点自己就是最大的，不需要加上左右子树的路径

2.根节点加上左子树的最大路径是最大

3.根节点加上右子树的最大路径是最大的

4.根节点加上左右子树的最大路径是最大的

我们每次判断下这几个变量的最大值，就是以当前节点为根节点的路径的最大值

现在我们看下-10这个节点，当求以这个节点为根节点的路径的最大值时，我们需要的是左子树路径的最大值和右子树路径的最大值，对于右子树来说它的路径的最大值为max(root.val, root.val+left_max, root.val+right_max)，即max（20,20+15,20+7），左子树同理

经过一次dfs即可求得结果
'''
class Solution:
    def maxPathSum(self, root):
        # write code here
        if not root:
            return 0

        self.max_value = float('-inf')

        def dfs(root):
            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)
            self.max_value = max(self.max_value, root.val + max_left, root.val + max_right,
                                 root.val + max_left + max_right)
            return max(0, max(max_left, max_right) + root.val)

        dfs(root)
        return self.max_value