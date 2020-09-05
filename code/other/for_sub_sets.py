class Solution:
    def forSubSets(self, list_):
        '''
        找一个集合的子集
        :param list_:
        :return:
        '''
        res = []

        def backtrack(track, choose_list):
            '''
            回溯法
            :param track:
            :param choose_list:
            :return:
            '''
            if len(track) <= len(choose_list) and set(track) not in res:
                res.append(set(track[:]))

            for choose in choose_list:
                if choose in track:
                    continue

                track.append(choose)
                backtrack(track, choose_list)
                track.pop()

        backtrack([], list_)

        return res

s = Solution()
print(s.forSubSets([1, 2, 3]))
