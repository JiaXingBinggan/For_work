# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        迭代方法
        '''
        if not t1:
            return t2
        if not t2:
            return t1

        v_queue = [(t1, t2)]
        t1.val += t2.val

        while len(v_queue) >= 1:
            for _ in range(len(v_queue)):
                current_v1, current_v2 = v_queue.pop(0)
                if not current_v1 and not current_v2:
                    continue

                if current_v2.left:
                    if current_v1.left: # 当t1和t2均有左节点时，入栈，然后进入下一层遍历
                        current_v1.left.val += current_v2.left.val
                        v_queue.append((current_v1.left, current_v2.left))
                    else: # 当只有t2有左节点时，直接将t2的左节点赋值过去（不需要遍历，因为是直接覆盖）
                        current_v1.left = current_v2.left

                if current_v2.right:
                    if current_v1.right: # 同左节点思路
                        current_v1.right.val += current_v2.right.val
                        v_queue.append((current_v1.right, current_v2.right))
                    else:
                        current_v1.right = current_v2.right

        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        递归方法
        '''
        if not t1:
            return t2
        if not t2:
            return t1

        root = TreeNode(t1.val + t2.val)

        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)

        return root


