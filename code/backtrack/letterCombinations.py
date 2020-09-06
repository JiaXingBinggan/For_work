class Solution(object):
    def letterCombinations(self, digits):
        """
        https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        num_alpha_dict = {'2': list('abc'), '3': list('def'), '4': list('ghi'), '5': list('jkl'), '6': list('mno'),
                          '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}

        res = []
        l = len(digits)
        def backtrack(s, temp):
            if not s and len(temp) == l and ''.join(temp[:]) not in res:
                res.append(''.join(temp[:]))

            for j, c in enumerate(s):
                if c in num_alpha_dict:
                    i = 0
                    while i < len(num_alpha_dict[c]):
                        temp.append(num_alpha_dict[c][i])
                        backtrack(s[j + 1:], temp)
                        temp.pop()
                        i += 1
                else:
                    continue

        backtrack(digits, [])

        return res
