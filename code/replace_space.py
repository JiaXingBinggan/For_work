class Solution(object):
    def replaceSpace(self, s):
        """
        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
        :type s: str
        :rtype: str
        """
        # 在 Python 和 Java 等语言中，字符串都被设计成不可变的类型，即无法直接修改字符串的某一位字符，需要新建一个字符串实现。
        new_s = ''
        for c in s:
            if c == ' ':
                new_s += '%20'
            else:
                new_s += c

        return new_s