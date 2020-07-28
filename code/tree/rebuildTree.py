class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        根据一棵树的前序遍历与中序遍历构造二叉树。
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root_val = preorder[0] # 前序遍历的第一个值一定是根节点
        root = TreeNode(root_val)

        inorder_root_index = inorder.index(root_val) # 找到中序遍历的根节点
        root.left = self.buildTree(preorder[1: inorder_root_index + 1], inorder[:inorder_root_index]) # 根节点的左子树，返回的是根节点左子树的根节点
        root.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:]) # 根节点的右子树，返回的是根节点右子树的根节点

        return root

    def buildTree2(self, inorder, postorder):
        '''
        根据一棵树的中序和后序遍历构造二叉树
        :param inorder:
        :param postorder:
        :return:
        '''
        if len(inorder) == 0:
            return None
        root_val = postorder[-1] # 后序遍历的最后一个数一定是根节点
        root = TreeNode(root_val)

        inorder_root_index = inorder.index(root_val) # 返回中序遍历中的root的位置
        
        root.left = self.buildTree2(inorder[0: inorder_root_index], postorder[0: inorder_root_index])
        root.right = self.buildTree2(inorder[inorder_root_index + 1:], postorder[inorder_root_index:-1])
        
        return root

    def preoder(self, root):
        if root == None:
            return []
        else:
            left = self.preoder(root.left)
            right = self.preoder(root.right)
            return [root.val] + left + right

    def inorder(self, root):
        if root == None:
            return []
        else:
            left = self.inorder(root.left)
            right = self.inorder(root.right)

            return left + [root.val] + right

    def postorder(self, root):
        if root == None:
            return []
        else:
            left = self.postorder(root.left)
            right = self.postorder(root.right)

            return left + right + [root.val]

s = Solution()
first_tree = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(s.preoder(first_tree))
print(s.inorder(first_tree))
print(s.postorder(first_tree))
second_tree = s.buildTree2([9,3,15,20,7], [9,15,7,20,3])
print(s.preoder(second_tree))
print(s.inorder(second_tree))
print(s.postorder(second_tree))
