class Tree:
    def __init__(self, data):
        self.key = data
        self.leftC = None
        self.rightC = None
        self.leftC_flag = 0
        self.rightC_flag = 0

        
class Solution:
    def reverseTree(self, alist):
        '''
        二叉树复原，https://www.icourse163.org/learn/PKU-1206307812?tid=1206626211#/learn/ojhw?id=1220971525
        :param alist:
        :return:
        '''
        tree = self.list2tree(alist)
        post_tree = self.inorder(tree)
        print(' '.join(tuple(post_tree)))

    def inorder(self, tree):
        if tree == None:
            return []
        else:
            left = self.inorder(tree.leftC)
            key = [str(tree.key)]
            right = self.inorder(tree.rightC)

            return left + key + right

    def list2tree(self, alist):
        tree = Tree(alist[0])

        return_tree = tree # tree的引用

        parent_stack = [tree]
        i = 1
        while i < len(alist) and len(parent_stack) > 0:
            tree = parent_stack.pop(0)
            if alist[i] != None:
                if tree.leftC_flag == 0 and tree.rightC_flag == 0:
                    new_tree = Tree(alist[i])
                    tree.leftC = new_tree
                    tree.leftC_flag = 1
                    parent_stack.append(tree.leftC)
                    parent_stack.insert(0, tree) # 始终要把父节点放在最左边
                    i += 1
                elif tree.leftC_flag == 1 and tree.rightC_flag == 0:
                    # print(alist[i])
                    new_tree = Tree(alist[i])
                    tree.rightC = new_tree
                    tree.rightC_flag = 1
                    parent_stack.append(tree.rightC)
                    i += 1
                else:
                    i = i
            else:
                if tree.leftC_flag == 0 and tree.rightC_flag == 0:
                    tree.leftC_flag = 1
                    parent_stack.insert(0, tree)
                elif tree.leftC_flag == 1 and tree.rightC_flag == 0:
                    tree.rightC_flag = 1
                i += 1

        return return_tree # 不能直接返回tree，因为最后的时候tree只是一个子树，应该返回原始tree的引用。
            
s = Solution()
print(s.reverseTree([5, 4, 7, 3, None, 2, None, -1, None, 9]))
# print(' '.join(s.reverseTree(tuple([5, 4, 7, 3, None, 2, None, -1, None, 9]))))