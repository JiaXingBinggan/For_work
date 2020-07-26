class Solution:
    def bubbleSort1(self, unordered_list):
        '''
        冒泡排序
        :param unordered_list: 无序表
        :return: 有序表
        '''
        for i in range(len(unordered_list) - 1):
            for j in range(len(unordered_list) - 1):
                temp = unordered_list[j + 1]
                if unordered_list[j] > temp:
                    unordered_list[j + 1] = unordered_list[j]
                    unordered_list[j] = temp

        ordered_list = unordered_list

        return ordered_list

    def bubbleSort2(self, unordered_list):
        '''
        对前面的改进，因为经过每一趟过后，列表的第n-1, n-2...个数均为最大、次大...的数
        :param unordered_list: 无序表
        :return: 有序表
        '''
        for i in range(len(unordered_list) - 1, 0, -1): # 趟数的编号，因为总共需要n-1趟，所有直接从n-1开始
            for j in range(i): # 每一趟的最后一位已经为最大、次大...的数了，不需要再进行排序，可以节省时间
                temp = unordered_list[j + 1]
                if unordered_list[j] > temp:
                    unordered_list[j + 1] = unordered_list[j]
                    unordered_list[j] = temp
                    # 或者unordered_list[j + 1], unordered_list[j] = unordered_list[j], unordered_list[j + 1]python支持直接交换

        ordered_list = unordered_list

        return ordered_list

    def bubbleSort3(self, unordered_list):
        '''
        对前面的改进，因为经过每一趟过后，列表的第n-1, n-2...个数均为最大、次大...的数，但是如果某一趟比对均没有发生交换， 则可提前结束
        该“短路”方法高度依赖于数据的初始布局，如果数据布局的随机读很高，造成每趟比对都会发生交换的话，就没有优势。还要额外付出一个is_exchange和相应赋值语句的代价。
        :param unordered_list: 无序表
        :return: 有序表
        '''
        is_exchange = True # 用于判断某趟排序是否发生了交换，如果均没发生，则可提前结束
        pass_num = len(unordered_list) - 1 # 排序趟数

        while pass_num > 0 and is_exchange:
            is_exchange = False
            for i in range(pass_num):
                temp = unordered_list[i + 1]
                if temp < unordered_list[i]:
                    is_exchange = True
                    unordered_list[i + 1] = unordered_list[i]
                    unordered_list[i] = temp

            pass_num -= 1

        ordered_list = unordered_list

        return ordered_list

s = Solution()
print(s.bubbleSort1([4, 23, 2, 7, 1, 5, 18]))
print(s.bubbleSort2([4, 23, 2, 7, 1, 5, 18]))
print(s.bubbleSort2([4, 23, 2, 7, 1, 5, 18]))

