# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        n_queue = [root]
        visited = set()
        visited.add(root)
        step = 1

        while len(n_queue) > 0:
            for i in range(len(n_queue)):  # 需要一层一层的遍历的时候
                current_n = n_queue.pop(0)

                if not current_n.left and not current_n.right:
                    return step

                if current_n.left and current_n.left not in visited:
                    n_queue.append(current_n.left)

                if current_n.right and current_n.right not in visited:
                    n_queue.append(current_n.right)

            step += 1  # 一层遍历完了才加1

        return step