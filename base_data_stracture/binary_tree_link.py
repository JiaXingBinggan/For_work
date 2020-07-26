class BinaryTree:
    '''
    二叉树的链表实现
    '''
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None # 初始化为空
        self.rightChild = None # 初始化为空

    def insertLeft(self, newNodeValue):
        new_node = BinaryTree(newNodeValue)
        if self.leftChild == None:
            self.leftChild = new_node
        else:
            new_node.leftChild = self.leftChild # 顺序不能颠倒
            self.leftChild = new_node

    def insertRight(self, newNodeValue):
        new_node = BinaryTree(newNodeValue)
        if self.rightChild == None:
            self.rightChild = new_node
        else:
            new_node.rightChild = self.rightChild # 顺序不能颠倒
            self.rightChild = new_node

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def getRoot(self):
        return self.key

    def setRootValue(self, new_value):
        self.key = new_value

    def preorder(self):
        '''
        前序遍历
        :return:
        '''
        print(self.getRoot())
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        '''
        后序遍历
        :return:
        '''
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
        print(self.getRoot())

    def inorder(self):
        '''
        中序遍历
        :return:
        '''
        if self.leftChild:
            self.leftChild.preorder()
        print(self.getRoot())
        if self.rightChild:
            self.rightChild.preorder()

def preorder(tree):
    '''
    前序遍历，根节点->左子树->右子树
    :return:
    '''
    if tree:
        print(tree.getRoot())
        preorder(tree.getLeft())
        preorder(tree.getRight())

def postorder(tree):
    '''
    后序遍历，左子树->右子树->根节点
    :param tree:
    :return:
    '''
    if tree:
        preorder(tree.getLeft())
        preorder(tree.getRight())
        print(tree.getRoot())

def inorder(tree):
    '''
    中序遍历：左子树->根节点->右子树
    :param tree:
    :return:
    '''
    if tree:
        preorder(tree.getLeft())
        print(tree.getRoot())
        print(preorder(tree.getRight()))
