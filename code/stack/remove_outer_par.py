# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        v_queue = [[t1, t2]]

        while len(v_queue) >= 1:
            for _ in range(len(v_queue)):
                current_t1, current_t2 = tuple(v_queue.pop(0))

                if current_t1 and current_t2:
                    current_t1.val += current_t2.val
                elif not current_t1 and current_t2:
                    current_t1 = TreeNode(current_t2.val)

                left_queue = []
                if current_t1.left:
                    left_queue.append(current_t1.left)
                else:
                    left_queue.append(None)
                
                if current_t2.left:
                    left_queue.append(current_t2.left)
                else:
                    left_queue.append(None)

                right_queue = []
                if current_t1.right:
                    right_queue.append(current_t1.right)
                else:
                    right_queue.append(None)

                if current_t2.right:
                    right_queue.append(current_t2.right)
                else:
                    right_queue.append(None)

                

                v_queue.append(left_queue)
                v_queue.append(right_queue)
        
        return t1



