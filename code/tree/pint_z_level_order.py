# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#
'''
题目描述
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树之字形层序遍历的结果是

    [
    [3],
    [20,9],
    [15,7]
    ]
'''
class Solution:
    def zigzagLevelOrder(self, root):
        # write code here
        if not root:
            return []

        v_queue = [root]

        res = [[root.val]]
        level = 2
        while len(v_queue) > 0:
            current_res = []
            for _ in range(len(v_queue)):
                v = v_queue.pop(0)
                if v.left:
                    v_queue.append(v.left)
                    if level % 2 == 0:
                        current_res.insert(0, v.left.val)
                    else:
                        current_res.append(v.left.val)

                if v.right:
                    v_queue.append(v.right)
                    if level % 2 == 0:
                        current_res.insert(0, v.right.val)
                    else:
                        current_res.append(v.right.val)
            level += 1
            if current_res:
                res.append(current_res)
        return res
