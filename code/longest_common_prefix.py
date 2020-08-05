class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # 字典序方法，https://blog.csdn.net/HappyRocking/article/details/83619392
        str0 = min(strs)
        # print(str0)
        str1 = max(strs)

        # 取出字符串的最大最小，就已经通过min和max就把字符串的相同项归类了，再输出不同值之前的相同项
        # print(str1)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # 取最小字符串然后，逐个比对方法
        min_len_str = sorted([[str_, len(str_)] for str_ in strs], key=lambda s: s[1])[0][0]
        strs.remove(min_len_str)

        longest_prefix = ''
        is_exist = True
        for i in range(len(min_len_str)):
            current_prefix = min_len_str[:i + 1]
            for str_ in strs:
                if str_[:i + 1] == current_prefix:
                    continue
                else:
                    is_exist = False
                    break
            if is_exist:
                longest_prefix = current_prefix

        return longest_prefix

    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        longest_prefix = ''
        for str_list in zip(*strs): # zip函数方法
            if len(set(str_list)) == 1:
                longest_prefix += str(str_list[0])
            else:
                break

        return longest_prefix

s = Solution()
print(s.longestCommonPrefix(['flight', 'flow', 'floww']))