class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftC = None
        self.rightC = None
        self.leftC_flag = 0 # 用于表示是否已有左子节点
        self.rightC_flag = 0

class Solution:
    def hierachicalTree(self, list):
        '''
        层次遍历序列还原为二叉树
        :param list: 层次遍历序列
        :return:
        '''
        current_tree = BinaryTree(list[0]) # 初始化一个最初的二叉树
        queue = [current_tree] # 节点序列

        return_tree = current_tree # 获取一个对树的引用

        i = 1
        while i < len(list) and len(queue) > 0: # 至少要有一个节点正在接受遍历
            current_tree = queue.pop(0) # 获取当前父节点
            if list[i] == None: # 如果值为空，则不需要对子节点进行更新
                if current_tree.leftC_flag == 0 and current_tree.rightC_flag == 0: # 如果左右两个子节点都没有数字，并且当前数字值为空，则继续遍历，但不新增节点
                    current_tree.leftC_flag = 1
                    queue.insert(0, current_tree) # 始终要把父节点放在最左边
                elif current_tree.leftC_flag == 1 and current_tree.rightC_flag == 0:
                    current_tree.rightC_flag = 1 # 设为1，表示已经遍历过，但不新增节点
                i += 1
            else:
                if current_tree.leftC_flag == 0 and current_tree.rightC_flag == 0: # 如果当前数字值不为空，则先增加左子节点
                    current_tree.leftC = BinaryTree(list[i])
                    current_tree.leftC_flag = 1
                    queue.append(current_tree.leftC_flag) # 为了下一步再从左子节点开始
                    queue.insert(0, current_tree) # 始终要把父节点放到左边
                    i += 1
                elif current_tree.leftC_flag == 1 and current_tree.rightC_flag == 0: # 如果左节点已有，则增加右子节点
                    current_tree.rightC = BinaryTree(list[i])
                    current_tree.rightC_flag = 1
                    queue.append(current_tree.rightC) # 只有当左子节点遍历完了，才弄右子节点，所有直接添加至末尾
                    i += 1

        return return_tree

