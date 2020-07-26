class Solution:
    def M2N(self, num, m, n):
        '''
        :param num: m进制的数字num
        :param m: m进制
        :param n: n进制
        :return: n进制的数字
        '''
        num_base_ten = self.m2ten(num, m)
        return self.Ten2N(num_base_ten, n)

    def Ten2N(self, num, n):
        '''
        :param num: 10进制的数字num
        :param n: n进制
        :return: n进制的数字
        '''
        convertString = '0123456789ABCDEF'
        if num < n:
            return convertString[num]
        else:
            return self.Ten2N(num // n, n) + convertString[num % n]

    def m2ten(self, num, m):
        '''
        :param num:
        :param m:
        :return: 10进制的数字
        '''
        num_base = 1 # 起始级别为个位
        while num >= 10 ** num_base:
            num_base += 1

        num_base_ten = 0
        for i in range(num_base):
            last_num = (num // 10 ** i) % 10
            num_base_ten = num_base_ten + last_num * (m ** i)

        return num_base_ten

s = Solution()
print(s.M2N(473, 8, 16))
