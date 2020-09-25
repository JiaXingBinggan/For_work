class HeapSort:
    def __init__(self, arr):
        self.heap_list = [0] + arr
        self.heap_size = len(arr)
        i = self.heap_size // 2

        while i > 0:
            self.down(i)
            i -= 1

    def down(self, index):
        while (index * 2) <= self.heap_size:
            min_child_index = self.minChildIndex(index)

            if self.heap_list[index] > self.heap_list[min_child_index]:
                self.heap_list[index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[index]

            index = min_child_index

    def minChildIndex(self, index):
        if (index * 2 + 1) > self.heap_size:
            return index * 2
        else:
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2 + 1
            else:
                return index * 2

    def delMin(self):
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_size -= 1
        self.heap_list.pop()
        self.down(1)
        return min_value

    def heap_sort(self):
        res = []
        while self.heap_size:
            res.append(self.delMin())

        return res

    def insert(self, item):
        self.heap_list.append(item)
        self.heap_size += 1
        self.rise()

    def rise(self):
        i = self.heap_size

        while i > 0:
            parent_index = i // 2
            if self.heap_list[parent_index] > self.heap_list[i]:
                self.heap_list[parent_index], self.heap_list[i] = self.heap_list[i], self.heap_list[parent_index]

            i = i // 2

h = HeapSort([4, 3, 2, 3, 15, 21, 7, 16, 9, 8])
h.insert(6)
print(h.heap_list)
print(h.heap_sort())