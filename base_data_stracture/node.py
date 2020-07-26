class Node:
    def __init__(self, data): # 链表中最核心的内容：node
        self.data = data # 初始化数据项
        self.next = None # 初始化下一个节点的指向信息为None

    def getData(self): # 获取当前节点数据项
        return self.data

    def getNext(self): # 获取下一个节点的指向信息
        return self.next

    def setData(self, newdata): # 设置节点的数据项
        self.data = newdata

    def setNext(self, newnext): # 设置下一个节点的指向信息
        self.next = newnext