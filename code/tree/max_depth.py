class Solution(object):
    def maxDepth(self, root):
        """
        给定一个二叉树，找出其最大深度。
        二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [[root, 0]] # 一定要记录当前节点所处的level
        depth = 1
        while len(queue) > 0: # 采用BFS的方法逐层遍历
            current_item = queue.pop(0)
            current_node = current_item[0]
            current_node_level = current_item[1]

            if current_node.left or current_node.right:
                if current_node.left:
                    queue.append([current_node.left, current_node_level + 1])

                if current_node.right:
                    queue.append([current_node.right, current_node_level + 1])

                depth = current_node_level + 2

        return depth

    def maxDepth2(self, root):
        '''
        更优解法，使用递归，因为当前root节点的深度=max(左子树的深度, 右子树) + 1
        :param root:
        :return:
        '''
        if not root: # 没有子节点了说明深度为0
            return 0

        return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1