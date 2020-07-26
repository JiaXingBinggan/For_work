class Solution:
    def postMultipleTree(self, tree):
        '''
        给定以嵌套列表形式给出的多叉树，求它的后序遍历
        注：每个代表非空多叉树的列表包含至少一项；列表第一项代表节点值，其后每一项分别为子树；遍历子树时以列表下标从小到大的顺序进行
        :param tree:
        :return:
        '''
        if len(tree) == 1: # 结束条件
            return tree
        else:
            result = []
            for i in range(1, len(tree)): # 后序遍历从左至右依次计算
                result += self.postMultipleTree(tree[i])
            result += [tree[0]] # 最后添加根节点

            return result

s = Solution()
print(s.postMultipleTree([1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]))