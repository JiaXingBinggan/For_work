class Solution:
    def printNumbers(self, n: int) -> [int]:
        '''
        打印 “从 1至最大的 n 位数的列表”
        常规思路就是用list(range(1, n))直接打印
        但是当n比较大时，它会超出int32整型的取值范围，超出取值范围的字无法正常存储。因此需要考虑大数越界问题。

        注意：我们可以观察到该列表是一个n位0-9的全排列，该列全排列的问题都可以使用这个代码来写
        :param n:
        :return:
        '''
        def dfs(x): # 深度遍历
            if x == n: # 递归结束条件2
                res.append(self.removeFirstZero(''.join(num))) # 获取当前完整的数字字符串
                return
            else:
                for i in range(10): # 每一位由0-9的数字构成
                    num[x] = str(i) # 获取当前位次的数字
                    dfs(x + 1) # 递归深度遍历下一位

        res = []
        num = ['0'] * n # 设置一个长度为n的数字数组，用于表示共多少位数字，num = ['0', '0']，如果数字11，则num = ['1', '1']
        dfs(0) # 从最高位开始（在数组中第0位表示最高位）

        return res

    def removeFirstZero(self, num_str):
        '''
        移除数字字符串前面的0
        :param num_str:
        :return:
        '''
        if int(num_str) == 0:
            return '0'

        i = 0
        done = False
        while i < len(num_str) and not done:
            if num_str[i] != '0':
                done = True
            i += 1

        return num_str[i - 1:]

s = Solution()
print(s.printNumbers(3))