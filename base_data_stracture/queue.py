class Queue:
    def __init__(self):
        self.items = [] # 实现的是list开头为队首，list末尾为队尾；如果反过来， 则时间复杂度相反

    def enqueue(self, item):
        self.items.append(item)
        # self.items.insert(0, item)

    def dequeue(self): # 先进先出
        return self.items.pop(0)
        # return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)