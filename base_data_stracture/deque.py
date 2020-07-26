class Deque:
    def __init__(self): # 双端队列的初始化
        self.items = [] # 以list作为实现的基准，左边为队首，右边为队尾

    def addFront(self, item): # 在队首加入item
        self.items.insert(0, item)

    def addRear(self, item): # 在队尾加入item
        self.items.append(item)

    def removeFront(self): # 移除队首
        return self.items.pop(0)

    def removeRear(self): # 移除队尾
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)