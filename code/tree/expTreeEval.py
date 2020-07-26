from base_data_stracture import binary_tree_link, stack

class Solution:
    def expParseTree(self, exp_str):
        '''
        将字符串表达式，转换为表达式解析树
        :param exp_str: 字符串表达式
        :return: 表达式解析树
        '''
        print(exp_str)
        exp_split = exp_str.replace(' ', '')
        parent_stack = stack.Stack()
        exp_binary_tree = binary_tree_link.BinaryTree('')
        parent_stack.push(exp_binary_tree) # 第一步就要先把当前父节点入栈
        current_tree = exp_binary_tree
        for s in exp_split:
            if s == '(': # 为左括号，创建左节点，当前节点下降
                current_tree.insertLeft('')
                parent_stack.push(current_tree) # 下降前必须把当前节点入栈
                current_tree = current_tree.getLeft()
            elif s not in '+-*/()': # 如果为操作数，则将当前节点赋值为操作数，并上升到父节点
                current_tree.setRootValue(int(s))
                parent_node = parent_stack.pop()
                current_tree = parent_node
            elif s in '+-*/': # 如果为操作符，则将当前节点赋值为操作符，并创建右节点，下降至其右节点
                current_tree.setRootValue(s)
                current_tree.insertRight('')
                parent_stack.push(current_tree) # 下降前必须把当前节点入栈
                current_tree = current_tree.getRight()
            elif s == ')': # 如果为右括号，则不断弹栈，获得父节点
                current_tree = parent_stack.pop()
            else: # 如果输入不合法字符返回错误
                raise ValueError

        return exp_binary_tree

    def expEval(self, exp_binary_tree):
        '''
        使用递归算法来求算数表达式
        其实该过程是树的后序遍历
        :param exp_binary_tree: 表达式解析树
        :return:
        '''
        left_tree = exp_binary_tree.getLeft() # 缩小规模
        right_tree = exp_binary_tree.getRight()

        if left_tree and right_tree:
            return self.mathFunction(exp_binary_tree.getRoot(), self.expEval(left_tree), self.expEval(right_tree)) # 递归迭代，调用自身
        else: # 基本结束条件，当到叶节点时，直接返回其key
            return exp_binary_tree.getRoot()

    def mathFunction(self, op, op_num1, op_num2):
        '''
        数学算法
        :param op: 操作符
        :param op_num1: 操作数1
        :param op_num2: 操作数2
        :return:
        '''
        if op == '+':
            return op_num1 + op_num2
        elif op == '-':
            return op_num1 - op_num2
        elif op == '*':
            return op_num1 * op_num2
        else:
            try:
                return op_num1 / op_num2
            except:
                print('illegal operator')
                raise ZeroDivisionError

    def tree2eval(self, exp_binary_tree):
        '''
        将表达式解析树转换成原来的全括号表达式，利用中序遍历递归
        :param exp_binary_tree:
        :return:
        '''
        eval = ''

        if exp_binary_tree:
            if exp_binary_tree.leftChild:
                eval = '(' + self.tree2eval(exp_binary_tree.getLeft())
            eval = eval + str(exp_binary_tree.getRoot())
            if exp_binary_tree.rightChild:
                eval = eval + self.tree2eval(exp_binary_tree.getRight()) + ')'

        return eval


s = Solution()
exp_binary_tree = s.expParseTree('(9 +(4 / 2))')
print(s.expEval(exp_binary_tree))
print(s.tree2eval(exp_binary_tree))