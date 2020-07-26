from base_data_stracture.node import Node

class OrderedList:
    def __int__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop: # 有序列表和无序列表不同的地方在于，如果提前遇到比当前item大的数，即可提前停止
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp_node = Node(item)
        if previous == None:
            temp_node.setNext(current)
            self.head = temp_node
        else:
            temp_node.setNext(current)
            previous.setNext(temp_node)

        self.size += 1

    def search(self, item):
        current = self.head
        has_item = False
        stop = False

        # 有序表的查找会节省很多时间，因为当当前节点的数据项大于item时，则说明后面的所有节点的数据项均大于item，则可提前停止
        while current != None and not has_item and not stop:
            if current.getData() == item:
                has_item = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return has_item

    def remove(self, item):
        previous = None
        current = self.head
        has_item = False
        stop = False

        while current != None and not has_item and not stop:
            if current.getData() == item:
                has_item = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()

        if has_item:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            return False

    def isEmpty(self):
        return self.size == 0
