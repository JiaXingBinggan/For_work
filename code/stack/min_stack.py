class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.items_ = []  # 辅助栈，存最小的

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        if not self.items_ or self.items_[-1] >= x:  # 当辅助栈最后一个元素大于或等于x时，可以添加
            self.items_.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.items.pop() == self.items_[-1]:  # 当栈顶元素相同时，都要出栈
            self.items_.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.items_[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()