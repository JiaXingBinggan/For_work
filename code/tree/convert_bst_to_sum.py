class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        sum_ = 0 # 保存一个最右侧的和
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right

            if stack:
                this = stack.pop()
                sum_ += this.val
                this.val = sum_
                cur = this.left

        return root