"""
用两个栈实现一个队列
"""
'''
1. 将stack1作为存储空间，将stack2作为临时缓冲区；也就是stack2辅助stack1做出队与入队操作；
2. 入队时，直接将元素压入stack1即可；
3. 出队时，将stack1中的元素依次出栈压入stack2中，再将stack2的栈顶元素弹出，最后将stack2中的元素再依次出栈压入stack1中，从而实现元素的出队，并返回弹出的元素；
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack1 == []:
            return None
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            out = self.stack2.pop()
            for j in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return out