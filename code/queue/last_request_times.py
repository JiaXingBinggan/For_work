from base_data_stracture.queue import Queue

'''
题目内容：计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。

输入格式:一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。

输出格式：一个与mylist等长的列表。

输入样例：[0,10,100,1000,10000,20000,100000]
输出样例：[1,2,3,4,5,2,1]
'''

class Solution:
    def lastRequestTimes(self, ordered_list):
        '''
        :param ordered_list: List
        :return: request times list
        '''
        request_time_list = [0] * len(ordered_list)
        ordered_num_queue = Queue()
        new_ordered_list = []

        for num in ordered_list: # 创建队列，用于比较队尾和队首的差距
            ordered_num_queue.enqueue(num)

        while not ordered_num_queue.isEmpty():
            first_num = ordered_num_queue.dequeue()
            new_ordered_list.append(first_num)

            if new_ordered_list[-1] - new_ordered_list[0] > 10000: # 判断队尾是否和队首的差距大于10000，如果大于1万，则要进入循环pop(0)操作
                while new_ordered_list[-1] - new_ordered_list[0] > 10000:
                    new_ordered_list.pop(0)
                request_time_list[ordered_list.index(first_num)] = len(new_ordered_list)
            else:
                request_time_list[ordered_list.index(first_num)] = len(new_ordered_list)

        return request_time_list

s = Solution()
print(s.lastRequestTimes([0,10,100,1000,10000,20000,100000]))
print(s.lastRequestTimes([0,10,100,1000,8000,8900,9999,19999,20000,100000]))
