class Solution(object):
    def addStrings(self, num1, num2):
        """
        给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

        提示：

            num1 和num2 的长度都小于 5100
            num1 和num2 都只包含数字 0-9
            num1 和num2 都不包含任何前导零
            你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
        :type num1: str
        :type num2: str
        :rtype: str
        """
        new_num1, new_num2 = [ord(c) - ord('0') for c in num1], [ord(c) - ord('0') for c in num2]

        sum_a = []
        add = 0
        for i in range(1, max(len(new_num1), len(new_num2)) + 1):
            n1 = new_num1[-i] if i <= len(new_num1) else 0
            n2 = new_num2[-i] if i <= len(new_num2) else 0 # 如果不够长则用零0填充

            sum_c = n1 + n2 + add
            sum_a.insert(0, str(sum_c % 10))
            add = sum_c // 10 # 记录是否有进位

        if add != 0:
            sum_a.insert(0, str(1))

        return ''.join(tuple(sum_a))


s = Solution()
print(s.addStrings('116123', '4959'))