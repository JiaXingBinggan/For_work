class Solution:
    def heapSort(self, alist):
        '''
        不基于已实现的二叉堆结构，直接实现
        :param alist:
        :return:
        '''
        head_list, heap_size = self.build_binary_heap(alist)

        orderedList = []
        while len(head_list) > 1:
            orderedList.append(self.delMin(head_list))

        return orderedList

    def delMin(self, heap_list):
        '''
        找到二叉堆最小值，并从二叉堆中删除
        :param heap_list:
        :return:
        '''
        min_key = heap_list[1]
        heap_list[1] = heap_list[-1]
        heap_list.pop()
        heap_size = len(heap_list) - 2
        self.down(heap_list, heap_size, 1)

        return min_key

    def build_binary_heap(self, alist):
        '''
        创建一个初始二叉堆
        :param alist:
        :return:
        '''
        i = len(alist) // 2 # 叶节点不需要下沉
        heap_list = [0] + alist
        heap_size = len(alist)
        while i > 0:
            self.down(heap_list, heap_size, i)
            i -= 1

        return heap_list, heap_size

    def down(self, heap_list, heap_size, index):
        '''
        二叉堆下沉操作，注意index均需从1开始，因为heap_list第0位为占位符
        :param heap_list: 表示二叉堆的列表
        :param heap_size:
        :param index:
        :return:
        '''
        while (index * 2) <= heap_size:
            min_c_i = self.min_child_index(heap_list, heap_size, index)
            if heap_list[index] > heap_list[min_c_i]: # 当当前节点的key大于较小子节点的key时，交换key值
                temp = heap_list[min_c_i]
                heap_list[min_c_i] = heap_list[index]
                heap_list[index] = temp
            else:
                break

            index = min_c_i # 当前节点转换到较小子节点

    def min_child_index(self, heap_list, heap_size, index):
        '''
        找当前节点的左右子节点，哪一个的key值更小，返回其下标
        :param heap_list:
        :param heap_size:
        :param index:
        :return:
        '''
        if (index * 2 + 1) > heap_size: # 不存在右节点时，直接返回左节点
            return index * 2
        else:
            if heap_list[index * 2] < heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

s = Solution()
print(s.heapSort([4, 3, 2, 15, 21, 7, 16, 9, 8]))