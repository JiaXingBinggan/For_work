class Solution(object):
    def restoreIpAddresses(self, s):
        """
        给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
        有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        res = []

        def check_s_valid(current_s):
            if not current_s:
                return False
            return int(current_s) <= 255 and str(int(current_s)) == current_s

        def recur_find_addr(current_s, current_res_=[]):
            if len(current_res_) == 3:
                if check_s_valid(current_s):
                    current_res_.append(current_s)  # 如果当前ip数组长度已经为3了后，直接把最后一个字符串给存到末尾
                    res.append('.'.join(tuple(current_res_[:])))
            else:
                for i in range(min(3, len(current_s))):
                    if check_s_valid(current_s[0:i + 1]):
                        recur_find_addr(current_s[i + 1:], current_res_ + [current_s[0: i + 1]])

        recur_find_addr(s)

        return res