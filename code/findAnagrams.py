class Solution:
    def findAnAgrams(self, s, p):
        '''
        给定一个字符串s与待查找字符串p，请给出使得s[i:i+len(p)]是p的一个字母重排的所有下标i
        题目保证字符串p非空
        :param s:
        :param p:
        :return:
        '''
        gap = len(p)
        p_letter_num_dict = self.cal_str_num(p)

        equal_list = []
        for i in range(0, len(s)):
            current_s_letter_num_dict = self.cal_str_num(s[i:i + gap])
            is_equal = True
            if len(p_letter_num_dict) == len(current_s_letter_num_dict):
                for key in p_letter_num_dict.keys():
                    try:
                        if current_s_letter_num_dict[key] != p_letter_num_dict[key]:
                            is_equal = False
                    except:
                        is_equal = False
            else:
                continue

            if is_equal:
                equal_list.append(i)

        return equal_list

    def cal_str_num(self, str_s):
        '''
        计算字符串中个字符出现的时间
        :param str_s:
        :return:
        '''
        letter_num_dict = {}
        for s in str_s:
            if letter_num_dict.get(ord(s)):
                letter_num_dict[ord(s)] += 1
            else:
                letter_num_dict.setdefault(ord(s), 1)

        return letter_num_dict

s = Solution()
print(s.findAnAgrams('cbaebabacd', 'abc'))
