# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
        例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7

        返回其层次遍历结果：

        [
          [3],
          [9,20],
          [15,7]
        ]
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res_list = [[root.val]]

        queue = [root]

        while len(queue) > 0:
            current_res = []
            for _ in range(len(queue)): # 一层一层的次序来打印
                current_node = queue.pop(0)
                if current_node.left:
                    queue.append(current_node.left)
                    current_res.append(current_node.left.val)

                if current_node.right:
                    queue.append(current_node.right)
                    current_res.append(current_node.right.val)

            if len(current_res) > 0:
                res_list.append(current_res)

        return res_list