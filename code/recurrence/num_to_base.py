class Solution:
    def numToBase(self, target_num, base):
        '''
        :param target_num: 需要转换进制的数
        :param base: 进制base-2，8，10，16
        :return: 对应进制的数
        '''
        convertString = '0123456789ABCDEF'
        if target_num < base:
            return convertString[target_num] # 如果小于10，直接返回对应位置的字符
        else:
            return self.numToBase(target_num // base, base) + convertString[target_num % base] # 递归思想


s = Solution()
print(s.numToBase(26, 2))
print(s.numToBase(64, 16))
