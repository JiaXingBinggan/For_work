def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    else:
        '''
       判断左右子树是否对称的第二种方法：利用对称二叉树的特性：前序遍历和后序遍历是正好相反的
       '''
        pre = self.preorder(root)
        post = self.postorder(root)
        i, j = 0, len(post) - 1
        while i < len(pre) and j >= 0:
            if pre[i] != post[j]:
                return False
            i += 1
            j -= 1

        return True

def preorder(self, root):
    if not root:
        return ['null']
    else:
        left = self.preorder(root.left)
        right = self.preorder(root.right)

        return [root.val] + left + right


def postorder(self, root):
    if not root:
        return ['null']
    else:
        left = self.postorder(root.left)
        right = self.postorder(root.right)

        return left + right + [root.val]