from base_data_stracture.node import Node

class UnorderedList:
    def __init__(self):
        self.head = None # 每一个无序表，都维护一个head，以指向node
        self.size = 0 # 初始化size为0

    def add(self, item): # 新增一个node，一般增加到最容易操作的位置，也就是head
        temp_node = Node(item)
        temp_node.setNext(self.head) # 要先把temp_node的next设为head，再把head设置temp_node，否则就会出现丢失链表信息的问题，因为你直接把head设为temp_node，而没有维护head后面的信息
        self.head = temp_node
        self.size += 1

    def size(self):
        return self.size
        # 另一种方法，但要繁琐一点
        # count = 0
        #
        # next = self.head
        # while next != None:
        #     next = next.getNext()
        #     count += 1
        #
        # return count

    def search(self, item):
        current = self.head

        has_item = False
        while current != None and not has_item:
            if current.getData() == item:
                has_item = True
            else:
                current = current.getNext() # 如果不等于，则继续遍历链表

        return has_item

    def remove(self, item): # 移除某个值
        previous = None
        current = self.head

        has_item = False
        while current != None and not has_item:
            if current.getData() == item:
                has_item = True
            else:
                previous = current
                current = current.getNext()

        if has_item:
            if previous == None: # 如果item就在表头，直接将head设置为当前节点的next
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext()) # 如果在中间，则直接将前一个节点的next设置为当前节点的next
        else:
            return False




