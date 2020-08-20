# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0

        def inorder(root):
            stack = []
            res = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                res.append(root.val)

                root = root.right

            return res

        def preorder(root):
            stack = []
            res = []
            while root or stack:
                while root:
                    res.append(root.val)
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                root = root.right

            return res

        def postorder(root):
            # 先遍历根节点，再遍历右子树，最后是左子树，这样就可以转化为和先序遍历一个类型了，最后只把遍历结果逆序输出就OK了。
            stack1 = []
            stack2 = []
            res = []
            while root or stack1:
                while root:
                    stack1.append(root)
                    stack2.append(root)
                    root = root.right
                root = stack1.pop()
                root = root.left

            while stack2:
                res.append(stack2.pop().val)

            return res

        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right