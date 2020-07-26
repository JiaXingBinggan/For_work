from base_data_stracture.queue import Queue

'''
题目内容：一开始给出了一个由小写字母组成的字符串 S。我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次
返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）。
输入格式:S。S为仅含有小写字母的字符串，长度不超过100000。

输出格式：一个与S等长的字符串。
输入样例："cba"
输出样例：acb
'''

class Solution:
    def compare_str(self, str):
        '''
        :param s: string
        :return: min string
        '''
        str_queue = Queue()
        for s in list(str): # 字符入队
            str_queue.enqueue(s)

        min_str = str
        trans_num = 0 # 用于计数，当queue循环一次后，queue中字符组成的字符串又变回原样
        while trans_num <= str_queue.size():
            first_str = str_queue.dequeue() # 队首出队
            str_queue.enqueue(first_str) # 将之前的队首入队
            new_str = ''.join(str_queue.items)

            if new_str < min_str:
                min_str = new_str

            trans_num += 1

        return min_str

s = Solution()
print(s.compare_str('cba'))


