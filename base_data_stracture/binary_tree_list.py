class BinaryTree:
    '''
    使用list类型来实现二叉树
    '''
    def init_tree(self, root_value):
        return [root_value, [], []]

    def inserLeft(self, binary_tree, left_value):
        temp_left = binary_tree.pop(1) # 首先取出左子树
        if len(temp_left) > 1:  # 如果已有左子树，则直接将left_value作为根节点，原有左子树作为left_value的左子树
            binary_tree.insert(1, [left_value, temp_left, []])
        else:
            binary_tree.insert(1, [left_value, [], []])

        return binary_tree

    def insertRight(self, binary_tree, right_value):
        temp_right = binary_tree.pop(2) # 首先取出右子树
        if len(temp_right) > 1: # 如果已有右子树，则直接将right_value作为根节点，原有左子树作为right_value的右子树
            binary_tree.insert(2, [right_value, [], temp_right])
        else:
            binary_tree.insert(2, [right_value, [], []])

        return binary_tree

    def getRootValue(self, binary_tree):
        return binary_tree[0]

    def setRootValue(self, binary_tree, new_value):
        binary_tree[0] = new_value

    def getLeftChid(self, binary_tree):
        return binary_tree[1]

    def getRightChild(self, binary_tree):
        return binary_tree[2]

# new_tree_object = BinaryTree()
# binary_tree = new_tree_object.init_tree(3) # 相当于定义了一个全局变量
# print(binary_tree)
# new_tree_object.inserLeft(binary_tree, 5)
# new_tree_object.inserLeft(binary_tree, 9)
# new_tree_object.insertRight(binary_tree, 4)
# new_tree_object.insertRight(binary_tree, 8)
# print(binary_tree)
#
# left_sub_tree = new_tree_object.getLeftChid(binary_tree)
# print(left_sub_tree)
# new_tree_object.setRootValue(left_sub_tree, 0, 1)
# print(binary_tree)
#
# new_tree_object.inserLeft(left_sub_tree, 2)
# print(binary_tree)