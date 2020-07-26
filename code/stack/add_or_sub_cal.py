class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        priorities = {}
        priorities['+']= 2
        priorities['-']= 2
        priorities['(']= 1

        token_list = list(s.strip(' '))
        op_stack = Stack() # 存储操作-栈
        op_num_stack = Stack() # 存储操作数-栈
        new_token_list = []
        temp_num = []

        for token in token_list:
            if token in '0123456789':
                temp_num.append(token)
            elif token in '*/+-()':
                if temp_num:
                    token_num = 0
                    for i, num in enumerate(temp_num):
                        token_num += int(num) * pow(10, len(temp_num) - i - 1)
                    temp_num = []
                    new_token_list.append(str(token_num))
                    new_token_list.append(token)
                else:
                    new_token_list.append(token)
        if temp_num:
            token_num = 0
            for i, num in enumerate(temp_num):
                token_num += int(num) * pow(10, len(temp_num) - i - 1)
            temp_num = []
            new_token_list.append(str(token_num))

        final = 0
        for token in reversed(new_token_list):
            if token in '0123456789':
                op_num_stack.push(token)
            elif token == ' ':
                continue
            elif token in ')':
                op_stack.push(token)
            elif token in '(':
                top_op = op_stack.pop()
                while top_op != ')':
                    operation1 = int(op_num_stack.pop()) # 栈顶的是第二个操作数
                    operation2 = int(op_num_stack.pop())
                    new_operation = self.math_function(top_op, operation1, operation2)
                    op_num_stack.push(new_operation)
                    top_op = op_stack.pop()

            elif token in '*/+-':
                # while not op_stack.isEmpty() and priorities[op_stack.peek()] >= priorities[token]:
                op_stack.push(token)
            elif int(token) >= 10:
                op_num_stack.push(token)

        while op_num_stack.size() >= 2:
            operation1 = int(op_num_stack.pop())  # 栈顶的是第二个操作数
            top_op = op_stack.pop()
            operation2 = int(op_num_stack.pop())
            new_operation = self.math_function(top_op, operation1, operation2)

            op_num_stack.push(new_operation)

        return int(op_num_stack.pop())

    def math_function(self, token, operation1, operation2):
        if token == '*':
            return operation1 * operation2
        elif token == '/':
            if operation2 == 0:
                return 'NAN'
            else:
                return int(operation1 / operation2)
        elif token == '+':
            return operation1 + operation2
        else:
            return operation1 - operation2


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
print(s.calculate('2-1+2'))
print(s.calculate('1-11'))
print(s.calculate('2-(5-6)'))
print(s.calculate('1-10'))
print(s.calculate('0-2147483647'))
print(s.calculate('(1+ (1 +2 ))'))
print(s.calculate('(1+(4+5+2)-3)+(6+8)'))