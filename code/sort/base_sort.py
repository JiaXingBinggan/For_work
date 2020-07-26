from base_data_stracture.queue import Queue

class Solution:
    def baseNumSort(self, unorderedList): # 基数排序，八大排序之一
        '''
        :param unorderedList: unordered list
        :return: ordered list
        '''
        orderedList = []
        queue_dict = {}
        for i in range(10):
            temp_queue = Queue()
            queue_dict.setdefault(i, temp_queue)

        max_num = max(unorderedList)
        max_base_index = 1 # 最大位数，起始位数为1
        main_queue = Queue()
        while max_num >= 10**max_base_index:
            max_base_index += 1

        for num in unorderedList:
            main_queue.enqueue(num)

        for i in range(max_base_index): # 最大数字不超过10**max_base_index，因此最多循环max_base_index次
            while not main_queue.isEmpty():
                current_num = main_queue.dequeue()
                base_index = int((current_num / 10 ** i) % 10) # 求基数，也就是十位数除以10，再对10取余；百位数除以百，再对10取余
                queue_dict[base_index].enqueue(current_num)

            for i in range(10):
                while not queue_dict[i].isEmpty():
                    main_queue.enqueue(queue_dict[i].dequeue())

        while not main_queue.isEmpty():
            orderedList.append(main_queue.dequeue())

        return orderedList

print(759 // 10)
s = Solution()
print(s.baseNumSort([8, 91, 34, 22, 65, 30, 4, 55, 18]))
