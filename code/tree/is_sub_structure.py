# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False

        bool_1 = self.judge(A, B) # 首先判断两个根节点是否相同
        bool_2 = self.isSubStructure(A.left, B) # 如果前者不同，则判断左子树是否存在
        bool_3 = self.isSubStructure(A.right, B) # 如果前两者都不同，则判断右子树是否存在

        return bool_1 or bool_2 or bool_3 # 只要有一个找到了匹配就可以得到True

    def judge(self, root, B):
        '''
        判断当前root节点是否和B相匹配
        :param root:
        :param B:
        :return:
        '''
        if not B: # 如果遍历后，B没有了，则说明之前的结果是匹配的，则返回True
            return True
        elif not root or root.val != B.val: # 第一个判断是判断是否存在和B同级的root，如果不存在则进入下一个判断，用于判断两者值是否相等
            return False
        else:
            return self.judge(root.left, B.left) and self.judge(root.right, B.right) # 当根节点root和B的值相同时，说明根节点匹配，则比对root和B的两个左、右子树是否匹配