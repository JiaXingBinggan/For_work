class Stack:
    def __init__(self):
        self.items = [] # 基于python中的list结构实现，栈底为self.items[0]，栈顶为self.items[-1]

    def isEmpty(self): # 栈是否为空
        return self.items == []

    def push(self, item): # 新增一个栈元素
        self.items.append(item)

    def pop(self): # 去除栈顶
        return self.items.pop() # 对于List来说就是删除最后一个值，pop还会返回删除的这个值

    def peek(self): # 观测栈顶，返回栈顶的数据项但不修改，栈不被修改
        return self.items[len(self.items) - 1]
        # return self.items[-1]

    def size(self):
        return len(self.items)