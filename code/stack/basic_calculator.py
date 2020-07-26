class Solution(object): # 基础计算器(leetcode 224)，中缀表达式转后缀表达式方法
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            int_s = int(s)
            return int_s
        except:
            post_fix = self.to_postfix(s)
            op_num_stack = Stack()
            token_list = list(post_fix)

            for token in token_list:
                if isinstance(token, int):
                    op_num_stack.push(token)
                elif token in '*/+-':
                    operation2 = int(op_num_stack.pop())
                    operation1 = int(op_num_stack.pop())
                    new_operation = self.math_function(token, operation1, operation2)
                    op_num_stack.push(str(new_operation))

            return int(op_num_stack.pop())

    def math_function(self, operator, operation1, operation2):
        if operator == '*':
            return operation1 * operation2
        elif operator == '/':
            if operation2 == 0:
                return 'NAN'
            else:
                return int(operation1 / operation2)
        elif operator == '+':
            return operation1 + operation2
        else:
            return operation1 - operation2

    def to_postfix(self, s):
        priorities = {}
        priorities['*'] = 3
        priorities['/'] = 3
        priorities['+'] = 2
        priorities['-'] = 2
        priorities['('] = 1

        op_stack = Stack()
        opearation_list = []
        token_list = list(s)
        new_token_list = []

        num = 0
        pow_ = 1
        for token in token_list:
            if token in '123456789':
                num = int(token) * pow_ + num
                pow_ *= 10
            elif token == '0':
                if pow_ != 1:
                    num = token + str(num)
                else:
                    num = token
                    pow_ *= 10
            elif token in '*/+-()':
                if pow_ != 1:
                    new_token_list.append(''.join(list(reversed(str(num)))))
                    num = 0
                    pow_ = 1
                new_token_list.append(token)
        if pow_ != 1:
            new_token_list.append(''.join(list(reversed(str(num)))))

        for token in new_token_list:
            if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
                opearation_list.append(int(token))
            elif token == ' ':
                continue
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_stack = op_stack.pop()
                while top_stack != '(':
                    opearation_list.append(top_stack)
                    top_stack = op_stack.pop()
            elif token in '*/+-':
                while not op_stack.isEmpty() and priorities[op_stack.peek()] >= priorities[token]:
                    opearation_list.append(str(op_stack.pop()))
                op_stack.push(token)
            elif int(token) >= 10:
                    opearation_list.append(int(token))

        while not op_stack.isEmpty():
            opearation_list.append(str(op_stack.pop()))

        return opearation_list

class Stack:
    def __init__(self):
        self.items = []  # 基于python中的list结构实现，栈底为self.items[0]，栈顶为self.items[-1]

    def isEmpty(self):  # 栈是否为空
        return self.items == []

    def push(self, item):  # 新增一个栈元素
        self.items.append(item)

    def pop(self):  # 去除栈顶
        return self.items.pop()  # 对于List来说就是删除最后一个值，pop还会返回删除的这个值

    def peek(self):  # 观测栈顶，返回栈顶的数据项但不修改，栈不被修改
        return self.items[len(self.items) - 1]
        # return self.items[-1]

    def size(self):
        return len(self.items)

s = Solution()
print(s.calculate("0-2147483647"))
print(s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))
print(s.calculate('1-11'))
print(s.calculate('2-(5-6)'))
print(s.calculate('1 + 1'))
print(s.calculate('(1+(4+15+2)-3)+(6+8)'))
# print(s.calculate('( A + B ) / C - ( D - E ) * ( F + G )'))
