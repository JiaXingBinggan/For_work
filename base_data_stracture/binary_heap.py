class BinaryHeap:
    def init_binary_heap(self):
        '''
        初始化一个空的二叉堆
        :return:
        '''
        self.heap_list = [0] # 首先设置一个零是为了更好的操作完全二叉树，使其满足如果当前节点的下标为p，则它的左子节点下标为2p，右子节点下标为2p+1，父节点下标为p//2
        self.current_size = 0 # 从0开始，因为self.head_list的第一位为0，是占位符

    def isEmpty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def insert(self, key):
        '''
        插入一个新key到二叉堆中。操作为：直接插入其到heap_list的末尾，但是这样会破坏二叉堆的堆次序，因此需要做一个“上浮rise”，逐步的还原二叉堆的堆次序
        :param key:
        :return:
        '''
        self.heap_list.append(key)
        self.current_size += 1
        self.rise()

    def rise(self):
        '''
        上浮操作，不断对比父节点和当前节点的key大小，如果父节点更大则交换，反之则不需要交换
        :return:
        '''
        i = self.current_size
        while i > 0:
            parent_index = i // 2
            if self.heap_list[parent_index] >= self.heap_list[i]:
                temp = self.heap_list[parent_index]
                self.heap_list[parent_index] = self.heap_list[i]
                self.heap_list[i] = temp
            else:
                break
            i = i // 2

    def finMin(self):
        '''
        返回堆中的最小项，其可以用于优先队列
        :return:
        '''
        return self.heap_list[1]

    def delMin(self):
        '''
        返回堆中的最小项，同时从堆中删除，其可以用于优先队列。操作：首先取出根节点，
        然后把heap_list的最后一项赋值到根节点，但是这样会破坏二叉堆的堆次序，因此需要一个“下沉down”操作，使得堆次序恢复
        :return:
        '''
        min_key = self.heap_list[1]
        self.current_size -= 1
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        self.down(1) # 因为把最后一个数字赋值到了根节点

        return min_key

    def down(self, index):
        while (index * 2) <= self.current_size: # 停止条件：至少还有左子节点
            min_chi_index = self.choose_min_child(index) # 选择左右子节点key更小的进行交换
            if self.heap_list[min_chi_index] < self.heap_list[index]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[min_chi_index]
                self.heap_list[min_chi_index] = temp
            else:
                break

            index = min_chi_index # 将当前节点更新到最小key的子节点

    def choose_min_child(self, index):
        if 2 * index + 1 > self.current_size: # 判断条件，如果右子节点index大于当前位置，说明没有右子节点，呼应前面的down函数中的(i * 2) <= self.current_size
            return 2 * index
        else:
            if self.heap_list[2 * index] > self.heap_list[2 * index + 1]:
                return 2 * index + 1
            else:
                return 2 * index

    def build_binary_heap(self, list):
        '''
        从已有的无序列表中创建一个，同样采用“下沉down”的思路，把大的值放到底层。此外，不需要从叶子节点开始
        :param list:
        :return:
        '''
        i = len(list) // 2 # 直接从内部节点开始，因为叶子节点不需要下沉
        self.heap_list = [0] + list
        self.current_size = len(list)
        while i > 0:
            self.down(i)
            i -= 1

# bh = BinaryHeap()
# bh.build_binary_heap([4, 2, 5, 7, 3, 1, 8])
# print(bh.heap_list)
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())

# bh = BinaryHeap()
# bh.init_binary_heap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
#
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())

