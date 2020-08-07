class Solution(object):
    def permutation(self, s):
        """
        输入一个字符串，打印出该字符串中字符的所有排列。
        你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        def backtrack(track_id, track, list_s):
            if len(track_id) == len(list_s):
                res.append(''.join(tuple(track[:])))

            for i, c in enumerate(list_s):  # list_s则为选择列表
                if i in track_id:  # 如果已经有在选择列表了则需要剪枝
                    continue

                track_id.append(i)
                track.append(c)
                backtrack(track_id, track, list_s)
                track_id.pop()  # 回溯，还原选择列表
                track.pop()

        res = []
        list_s = list(s)
        backtrack([], [], list_s)

        return list(set(res))
