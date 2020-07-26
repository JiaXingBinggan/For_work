from base_data_stracture.binary_heap import BinaryHeap

class Solution:
    def heap_sort(self, alist):
        '''
        堆排序，主要基于二叉堆（也可以是优先队列）
        :param alist: 无序列表
        :return:
        '''
        binary_heap = BinaryHeap()
        binary_heap.build_binary_heap(alist)

        orderedList = []
        while not binary_heap.isEmpty():
            orderedList.append(binary_heap.delMin())

        return orderedList

s = Solution()
print(s.heap_sort([4, 3, 2, 15, 21, 7, 16, 9, 8]))