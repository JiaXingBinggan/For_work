class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        s = s.strip()
        # 模拟思路
        met_dot = met_digit = met_e = False
        for i,char in enumerate(s):
            if char in ["+","-"]:
                if i > 0 and (s[i-1] != 'e' and s[i-1] != 'E'): # 说明前面不是科学计数法
                    return False
            elif char == '.':
                if met_dot or met_e: # 已有点号（重复），或者有e
                    return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or (not met_digit): # 是否已经获得了
                    return False
                met_e,met_digit = True,False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit